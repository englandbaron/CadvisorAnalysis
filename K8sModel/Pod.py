#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019/9/13 上午12:25
"""

class Pod(object):
    def __init__(self,name,cpu,memory):
        # TODO: Generate the Name/CPU/Memeory & Bind Utilization
        self.name = name
        self.cpu = cpu
        self.memory = memory

        self.UtilizationModel = None

    def get_capacity(self):
        # TODO: Return Capacity
        pass

    def get_service_mesh(self):
        # TODO: Return Service Object
        pass

    def __repr__(self):
        return "<Pod %s>" % (self.name)