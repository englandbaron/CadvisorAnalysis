#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: zzetian@cn.ibm.com
@software: PyCharm
@time: 2019-10-17 19:03
"""
import random
from algorithm.const import return_request_list, HostEnergy_Variables, HOST_NUMBER, POD_INITIAL_NUMBER_ON_EACH_HOST
from algorithm.Host import Host
from algorithm.Pod import Pod

request_list = return_request_list()
host_list = [Host(POD_INITIAL_NUMBER_ON_EACH_HOST,i % 4,random.choice(
    [i for i in range(len(HostEnergy_Variables))]
)) for i in range(HOST_NUMBER)]

# for host in host_list:
#     print(host)
#     for pod in host.podlist:
#         print(pod,end=" ")
#         print(pod.ReturnPodMIP())

for request in request_list:
    TotalPodCapacity = 0
    for host in host_list:
        for pod in host.podlist:
            Pod_MIP = pod.ReturnPodMIP()
            TotalPodCapacity = TotalPodCapacity + Pod_MIP
    # print(TotalPodCapacity, end= " ")
    # print(request)
    if request > TotalPodCapacity:
        print(request,end=" | ")
        print(TotalPodCapacity)

print(len(request_list))

def FirstFit():
    pass

def K8SLoadBalance():
    pass

def LRK8SLoadBalance():
    pass