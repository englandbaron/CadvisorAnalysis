#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-10-30 23:35
"""
from datetime import datetime
import dateutil.parser

def IsoTimeToUnixTime(isotime):
    return 1000000*datetime.timestamp(dateutil.parser.parse(isotime))

FILE = open("output")
file_line = FILE.readline()
DIC = {}

while file_line:
    file_split = file_line.split(" | ")
    print(file_split)
    time = int(IsoTimeToUnixTime(file_split[0].split('Time: ')[1]))
    cpu_score = float(file_split[1].split('CPU Score: ')[1])
    # memory = float(file_split[-1].split('memory: ')[1])
    txb = float(file_split[2].split('txb : ')[1])
    rxb = float(file_split[3].split('rxb: ')[1])
    DIC[time] = [cpu_score,txb,rxb]
    file_line = FILE.readline()

print(DIC)

from matplotlib import pyplot as plt
import matplotlib.gridspec as gridspec

gs = gridspec.GridSpec(2, 2)
fig = plt.figure()

x = [i for i in DIC.keys()]
cpu_y = []
txb_y = []
rxb_y = []
for key,value in DIC.items():
    cpu_y.append(DIC[key][0])
    txb_y.append(DIC[key][1])
    rxb_y.append(DIC[key][2])

cpu = fig.add_subplot(gs[0, :])
cpu.plot(x,cpu_y,'r')
plt.title('cpu Score')

txb = fig.add_subplot(gs[1, 0])
txb.plot(x,txb_y,'b')
plt.title('Txb')

rxb = fig.add_subplot(gs[1, 1])
rxb.plot(x,rxb_y)
plt.title('Rxb')

plt.legend()
plt.show()
