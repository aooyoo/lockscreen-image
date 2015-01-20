# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-18'

import os
import json


class ErrorCode(object):
    REQUEST_ERROR = 1
    NEED_LOGIN = 10
    FOREGROUND_NOT_EXIST = 20
    BACKGROUND_NOT_EXIST = 21

    LANGUAGE_MAP_ZH = {
        1: '请求错误',
        10: '需要重新登录',
        20: '找不到此前景图片',
        21: '找不到此背景图片',
    }

    @classmethod
    def gen_json(cls):
        from django.conf import settings

        DIR = os.path.dirname(settings.BASE_DIR)
        with open(os.path.join(DIR, 'errorcode.json'), 'w') as f:
            f.write(json.dumps(cls.LANGUAGE_MAP_ZH, indent=4))
