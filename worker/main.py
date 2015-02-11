# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-20'

import os
import sys


CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PARENT_PATH = os.path.normpath(os.path.join(CURRENT_PATH, '../project'))
sys.path.append(PARENT_PATH)

import re
import json
import zipfile
import datetime
from collections import defaultdict
from contextlib import contextmanager

import traceback

import beanstalkc
import sevencow
import requests
from mailgun2 import Mailgun

from project import settings


def log(text):
    print "{0}: {1}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text)

# 获取到的Job
# job = {
#     'zip': zip file path,
#     'callback_url': callback url,         处理完毕后将数据发送到此url
#     'callback_data': {},                  处理完毕后的数据+这个data = 最终要返回的数据
# }
#
#
# 获取到job后就是解析zip文件，上传cdn
# 压缩包格式
# xxx.zip
# |----i4
# |    |----1.png
# |    |----2.png
# |
# |----i5
# |    |----1.png
# |    |----2.png
#
#
# 返回的数据
#     {
#         callback_data in job if provide,
#         'images': [
#             # image 1
#             {
#                 'i4': key,
#                 'i5': key,
#                 ...
#             },
#             # image 2
#             {
#                 'i4': key,
#                 'i5': key,
#                 ...
#             },
#             ...
#         ]
#     }
#


IMAGE_PATTERN = re.compile('.+\.(jpg|JPG|jpeg|JPEG|png|PNG)\s*$')


class ImageUpload(object):
    def __init__(self):
        self.bean = beanstalkc.Connection(
            host=settings.BEAN_HOST,
            port=settings.BEAN_PORT
        )

        self.cow = sevencow.Cow(
            settings.QINIU_ACCESS_KEY,
            settings.QINIU_SECRET_KEY,
        )

        self.bucket = self.cow.get_bucket(settings.QINIU_BUCKET)

    @contextmanager
    def get_zipfile(self, zip_file):
        z = zipfile.ZipFile(zip_file)
        yield z
        z.close()


    def parse_zip(self, z):
        """

        :type z: zipfile.ZipFile
        """
        images = defaultdict(lambda :[])

        for name in z.namelist():
            if IMAGE_PATTERN.search(name) is None:
                continue

            image_name = os.path.basename(name)
            image_name = image_name.strip().lower()
            images[image_name].append(name)

        return images


    def upload(self, images, z):
        """

        :type images: dict
        :type z: zipfile.ZipFile
        """

        result = []
        for _, names in images.iteritems():
            one_image = {}
            for name in names:
                data = z.open(name).read()
                res = self.bucket.put(name, data=data)

                phone_types = name.split('/')[-2]
                phone_types = [x for x in phone_types.split('-')]
                for tp in phone_types:
                    one_image[tp] = res['key']

            result.append(one_image)

        return result



    def parse_zip_and_upload(self, zip_file):
        with self.get_zipfile(zip_file) as z:
            images = self.parse_zip(z)
            return self.upload(images, z)


    def feedback(self, callback_url, data):
        requests.post(callback_url, data=json.dumps(data))


    def process(self, job):
        log("---- New Job {0} ----".format(job.jid))
        log(job.body)
        data = json.loads(job.body)
        zip_file = data['zip']
        callback_url = data['callback_url']
        callback_data = data.get('callback_data', {})

        result_data = self.parse_zip_and_upload(zip_file)
        callback_data['images'] = result_data
        self.feedback(callback_url, callback_data)

        log("---- End Job {0} ----".format(job.jid))


    @classmethod
    def run(cls):
        self = cls()
        while True:
            job = self.bean.reserve()
            try:
                self.process(job)
            except:
                error_data = traceback.format_exc()
                log(error_data)

                to_mails = [admin[1] for admin in settings.ADMINS]
                mail = Mailgun(settings.MAILGUN_ACCESS_KEY, settings.MAILGUN_SERVER_NAME)
                mail.send_message(settings.SERVER_EMAIL, to_mails, subject="Worker Error", text=error_data)
            finally:
                job.delete()


if __name__ == '__main__':
    from daemonized import Daemonize

    arg = sys.argv[1]
    if arg == 'debug':
        ImageUpload.run()
    else:
        log_file = os.path.join(CURRENT_PATH, 'run', arg)

        @Daemonize(stdout=log_file, stderr=log_file)
        def run():
            ImageUpload.run()

        run()


