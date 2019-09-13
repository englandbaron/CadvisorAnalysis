#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019/9/13 上午12:25
"""

from .Pod import Pod

class Deployment(object):
    def __init__(self,name):
        # TODO: Logic View for Pods
        self.pod_list = []
        pass

    def pod_bind(self,pod):
        self.pod_list.append(pod)

    def __repr__(self):
        return "<Deployment %s>" % self.name