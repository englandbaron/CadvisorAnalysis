#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: zzetian@cn.ibm.com
@software: PyCharm
@time: 2019-08-02 19:17
"""
from __future__ import division
import dateutil.parser
from datetime import datetime

from CadvisorModel.ProjectWorkspace import ProjectWorkspace

# workspace = ProjectWorkspace("HTTP", "http://node1:8080")
workspace = ProjectWorkspace("FILE","2019_08_07_20_26_03/")
ContainerStatParser = workspace.ContainerStatParser()

for stats in ContainerStatParser.CollectList:
    # print([obj['time'] for obj in stats['STATS']])
    print("POD: %s | KEY: %s" % (stats['PODNAME'],stats['KEY']),end='')
    i = 0
    cur = stats['STATS'][-1]
    prev = stats['STATS'][-2]

    cur_timestamp = int(datetime.timestamp(dateutil.parser.parse(cur['time'])) * 1000)
    prev_timestamp = int(datetime.timestamp(dateutil.parser.parse(prev['time'])) * 1000)

    cur_total = cur['cpu_usage']
    prev_total = prev['cpu_usage']

    rawUsage = cur_total - prev_total
    intervalNs = (cur_timestamp - prev_timestamp) * 10000 #1025000000

    # print("intervalNs: ",intervalNs)
    # print("rawUsage: ",rawUsage)
    score = ((rawUsage/intervalNs)/2) * 100
    print(" | Score: %s" % score,end='')
    print(" | Time: %s" % cur['time'])
    print("=======================================================")