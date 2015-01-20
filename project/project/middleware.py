# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-18'

from django.http import JsonResponse
from project.exceptions import ProjectException
from project.errorcode import ErrorCode

NOT_CHECK_PATH = ['/admin', '/login', '/callback']
class CheckSessionMiddleware(object):
    # this middleware needs 'django.contrib.sessions.middleware.SessionMiddleware'
    # and MUST bellow it

    def process_request(self, request):
        for path in NOT_CHECK_PATH:
            if request.path.startswith(path):
                return None

        if request.session.get('udid', None) is None:
            data = {
                'ret': ErrorCode.NEED_LOGIN
            }
            return JsonResponse(data)




class ExceptionHandlerMiddleware(object):
    def process_exception(self, request, exception):
        if isinstance(exception, ProjectException):
            data = {
                'ret': exception.errno
            }
            return JsonResponse(data)

        import traceback
        traceback.print_exc()
        raise exception

