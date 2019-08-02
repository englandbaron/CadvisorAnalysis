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

from ToolUtils.PublicUtils import LOG
from CadvisorModel.ProjectWorkspace import ProjectWorkspace

workspace = ProjectWorkspace("HTTP", "http://node1:8080")
# workspace = ProjectWorkspace("FILE","2019_08_02_20_23_53/")
MachineStatParser, ContainerStatParser, SummaryStatParser = \
    workspace.MachineStatParser(), workspace.ContainerStatParser(), workspace.SummaryStatParser()

# LOG.success("MachineStats: %s" % MachineStatParser)
# for stat in MachineStatParser.CollectList:
#     print("%s | %s | %s |" % (stat['time'],stat['cpu_usage'],stat['cpu_percent']))
# LOG.success("ContainerStats: %s" % ContainerStatParser.CollectList)
for stats in ContainerStatParser.CollectList:
    print(stats['PODNAME'])
    print(stats['KEY'])
    i = 0
    cur = stats['STATS'][-1]
    prev = stats['STATS'][-2]

    cur_timestamp = int(datetime.timestamp(dateutil.parser.parse(cur['time'])) * 1000)
    prev_timestamp = int(datetime.timestamp(dateutil.parser.parse(prev['time'])) * 1000)
    # print("CUR: " , cur_timestamp)
    # print("PREV: " , prev_timestamp)

    cur_total = cur['cpu_usage']
    prev_total = prev['cpu_usage']

    rawUsage = cur_total - prev_total
    intervalNs = (cur_timestamp - prev_timestamp) * 10000 #1025000000

    # print("intervalNs: ",intervalNs)
    # print("rawUsage: ",rawUsage)
    print(((rawUsage/intervalNs)/2) * 100)
    print("===========")
    # for STAT in stats['STATS']:
        # print("%s | Time: %s | Cpu_Usage: %s" % (i,datetime.timestamp(dateutil.parser.parse(STAT['time'])) , STAT['cpu_usage']))
        # i = i + 1

# datestring = '2019-08-02T12:23:53.619494639Z '
# local_time = dateutil.parser.parse(datestring)
# print(datetime.timestamp(local_time), type(local_time))
# LOG.success("ContainerSummarys: %s" % SummaryStatParser)
