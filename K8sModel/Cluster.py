#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019/9/13 上午12:26
"""

from K8sCore import g

class K8SCluster(object):
    def __init__(self,NodeList,PredictAlgorithm,PriorityAlgorithm):
        # TODO: Cluster Initial Function
        self.Clock = 0.0
        while True:
            self.AutoClock()
        pass

    def GetStatus(self):
        # TODO: Get Cluster Status & Draw Plot
        pass

    def AutoClock(self):
        ClockPeriod = g.TimePeriod
        self.Clock = self.Clock + g.TimePeriod