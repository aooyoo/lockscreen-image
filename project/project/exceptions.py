# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '15-1-18'


class ProjectException(Exception):
    def __init__(self, errorno, *args, **kwargs):
        self.errno = errorno
        Exception.__init__(self, *args, **kwargs)
