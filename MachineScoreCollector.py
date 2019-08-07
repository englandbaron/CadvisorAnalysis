#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: zzetian@cn.ibm.com
@software: PyCharm
@time: 2019-08-02 19:17
"""
from __future__ import division
import sys
import argparse
import dateutil.parser
from datetime import datetime

from CadvisorModel.ProjectWorkspace import ProjectWorkspace
from ToolUtils import JsonParser,LOG

parser = argparse.ArgumentParser(description="Resource Fetching Method")
parser.add_argument('-m', '--method',help="""Resource Type(HTTP/FILE)""")
parser.add_argument('-i', '--item',help="""The Resource Item""")
args = parser.parse_args()
if not args.item:
    parser.print_help()
    sys.stderr.write("\nExample: \n  python ContainerScoreCollector.py -m HTTP -i http://node1:8080\n")
    sys.exit()
workspace = ProjectWorkspace(args.method, args.item)
MachineStatParser = workspace.MachineStatParser()

for mos in range(1,len(MachineStatParser.CollectList)):
    cur = MachineStatParser.CollectList[mos]
    # JsonParser.BeautifulOutput(cur)
    prev = MachineStatParser.CollectList[mos - 1]

    cur_timestamp = int(datetime.timestamp(dateutil.parser.parse(cur['time'])) * 1000)
    prev_timestamp = int(datetime.timestamp(dateutil.parser.parse(prev['time'])) * 1000)

    intervalNs = (cur_timestamp - prev_timestamp) * 10000

    #CPU
    cpu_cur_total = cur['cpu_usage']
    cpu_prev_total = prev['cpu_usage']

    rawUsage = cpu_cur_total - cpu_prev_total
    cpu_score = ((rawUsage / intervalNs) / 2) * 100

    #TXB
    txb_cur_total = cur['txb'][0]
    txb_prev_total = prev['txb'][0]
    rawUsage = txb_cur_total - txb_prev_total
    txb_rate = ((rawUsage / intervalNs) / 2) * 100

    #RXB
    rxb_cur_total = cur['rxb'][0]
    rxb_prev_total = prev['rxb'][0]
    rawUsage = rxb_cur_total - rxb_prev_total
    rxb_rate = ((rawUsage / intervalNs) / 2) * 100
    #Memory
    memory_usage = cur['memory']

    print("Time: %s | CPU Score: %s | txb : %s | rxb: %s | memory: %s" % (cur['time'],cpu_score,txb_rate,rxb_rate,memory_usage))