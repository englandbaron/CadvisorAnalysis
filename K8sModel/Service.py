#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019/9/13 上午12:25
"""
from ToolUtils.PublicUtils import LOG
from .Deployment import Deployment

class Service(object):
    def __init__(self,name,PodNumber,Seed):
        # TODO: Logic View for Service
        self.name = name
        self.PodNumber = PodNumber
        self.Seed = Seed
        self.Deployment = Deployment(name,PodNumber)
        LOG.debug("Service Initial: %s" % self.__repr__())

    def __repr__(self):
        return "<Service %s|%d|%d>" % (self.name,self.PodNumber,self.Seed)