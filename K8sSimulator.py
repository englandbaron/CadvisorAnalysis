#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-09-24 19:09
"""

from K8sCore.g import *
from K8sModel.Host import Host
from K8sModel.Service import Service

if __name__ == '__main__':
    NodeList = [
        Host("node1",HostMIP_Variables[0],HostMemory_Variables[0])
    ]

    ServiceList = [
        Service("WebFront",10,10001),
        Service("WebBackend",30,20002),
        Service("DB",3,30003),
    ]
    # cluster = K8SCluster()