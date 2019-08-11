#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-08-02 19:17
"""
from __future__ import division
import sys
import argparse
import dateutil.parser
from datetime import datetime

from CadvisorModel.ProjectWorkspace import ProjectWorkspace

parser = argparse.ArgumentParser(description="Resource Fetching Method")
parser.add_argument('-m', '--method',help="""Resource Type(HTTP/FILE)""")
parser.add_argument('-i', '--item',help="""The Resource Item""")
args = parser.parse_args()
if not args.item:
    parser.print_help()
    sys.stderr.write("\nExample: \n  python ContainerScoreCollector.py -m HTTP -i http://node1:8080\n")
    sys.exit()
workspace = ProjectWorkspace(args.method, args.item)
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