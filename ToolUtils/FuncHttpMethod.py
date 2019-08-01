#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-04-12 13:14
"""
import requests


def CheckConn():
    def func_wrapper(func):
        def HttpCheckConnection(self, *args, **kwargs):
            try:
                requests.get(self.API_URL).raise_for_status()
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
                ResponseResult = 0
            except requests.exceptions.HTTPError:
                ResponseResult = -1
            else:
                ResponseResult = 1
            return func(self, ResponseResult, *args, **kwargs)

        return HttpCheckConnection

    return func_wrapper


def GET(url, auth=None, verify=False):
    def func_wrapper(func):
        def HttpGetMethod(*args, **kwargs):
            Result = func(
                requests.get(
                    url, auth=auth, verify=verify
                ), *args
            )
            return Result

        return HttpGetMethod

    return func_wrapper


def POST(url, auth=None):
    def logging_decorator(func):
        def HttpPostMethod(*args, **kwargs):
            Result = func(kwargs,
                          requests.post(
                              url, auth=auth, data=args[1]
                          )
                          )
            return Result

        return HttpPostMethod

    return logging_decorator


def JsonPOST(url, auth=None):
    def logging_decorator(func):
        def HttpPostMethod(*args, **kwargs):
            Result = func(kwargs,
                          requests.post(
                              url, auth=auth, json=args[1]
                          )
                          )
            return Result

        return HttpPostMethod

    return logging_decorator
