#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-07-21 14:16
"""

from __future__ import division
from ToolUtils.PublicUtils import LOG


class MachinestatModel(object):
    def __init__(self, d):
        self.__dict__['machine'] = d

    def __getattr__(self, key):
        value = self.__dict__['machine'][key]
        if type(value) == type({}):
            return MachinestatModel(value)
        return value

    def INIT(self):
        self.CollectList = []
        for machineinfo in self.machine:
            DIC = {}
            DIC['time'] = machineinfo['timestamp']
            DIC['cpu_usage'] = machineinfo['cpu']['usage']['total']
            DIC['cpu_percent'] = machineinfo['cpu']['usage']['user'] / machineinfo['cpu']['usage']['total']
            DIC['cpu_nodes'] = machineinfo['cpu']['usage']['per_cpu_usage']
            DIC['txb'] = [network_interface['tx_bytes'] for network_interface in machineinfo['network']['interfaces'] if
                          network_interface['name'] in ['eth0']]
            DIC['rxb'] = [network_interface['rx_bytes'] for network_interface in machineinfo['network']['interfaces'] if
                          network_interface['name'] in ['eth0']]
            self.CollectList.append(DIC)
        return self


class ContainerModel(object):
    def __init__(self, d):
        self.__dict__['containerset'] = d

    def __getattr__(self, key):
        value = self.__dict__['containerset'][key]
        if type(value) == type({}):
            return MachinestatModel(value)
        return value

    def INIT(self):
        _CollectList = []
        for key, spec in self.containerset.items():
            StatsList = []
            if spec['spec'].get('labels', "UNKNOWN") != "UNKNOWN":
                for podinfo in spec['stats']:
                    DIC = {}
                    DIC['time'] = podinfo['timestamp']
                    DIC['cpu_usage'] = podinfo['cpu']['usage']['total']
                    # DIC['cpu_percent'] = podinfo['cpu']['usage']['user'] / podinfo['cpu']['usage']['total']
                    DIC['cpu_nodes'] = podinfo['cpu']['usage']['per_cpu_usage']
                    # POD Network
                    if podinfo.get('network', 'UNKNOWN') != "UNKNOWN":
                        DIC['txb'] = [network_interface['tx_bytes'] for network_interface in
                                      podinfo['network']['interfaces'] if network_interface['name'] in ['eth0']]
                        DIC['rxb'] = [network_interface['rx_bytes'] for network_interface in
                                      podinfo['network']['interfaces'] if network_interface['name'] in ['eth0']]
                    StatsList.append(DIC)

            if spec['spec'].get('labels', "UNKNOWN") != "UNKNOWN":
                _CollectList.append(
                    {"PODNAME": spec['spec'].get('labels').get("io.kubernetes.pod.name"), "KEY": key,
                     "STATS": StatsList})
        self.CollectList = []
        for item in _CollectList:
            _tmp_list = []
            STAT_LIST = item['STATS']
            for CPU in STAT_LIST:
                _tmp_list.append(CPU['cpu_usage'])
            if (len(list(set(_tmp_list)))) > 1:
                self.CollectList.append(item)
        return self


class ContainerSummaryModel(object):
    def __init__(self, d):
        self.__dict__['containersummary'] = d

    def __getattr__(self, key):
        value = self.__dict__['containersummary'][key]
        if type(value) == type({}):
            return MachinestatModel(value)
        return value

    def INIT(self):
        self.DIC = {}
        for key in [key for key, value in self.containersummary.items() if "/kubepods.slice/" in key]:
            self.DIC[key] = {
                "Hour": {
                    "CPU": {
                        "Mean": self.containersummary[key]['hour_usage']['cpu']['mean'],
                        "Fifty": self.containersummary[key]['hour_usage']['cpu']['fifty'],
                        "Ninety": self.containersummary[key]['hour_usage']['cpu']['ninety'],
                        "Ninetyfive": self.containersummary[key]['hour_usage']['cpu']['ninetyfive'],
                    },
                    "Memory": {
                        "Mean": self.containersummary[key]['minute_usage']['memory']['mean'],
                        "Fifty": self.containersummary[key]['minute_usage']['memory']['fifty'],
                        "Ninety": self.containersummary[key]['minute_usage']['memory']['ninety'],
                        "Ninetyfive": self.containersummary[key]['minute_usage']['memory']['ninetyfive'],
                    }
                },
                "Minute": {
                    "CPU": self.containersummary[key]['minute_usage']['cpu']['mean'],
                    "MEMORY": self.containersummary[key]['minute_usage']['memory']['mean']
                }
            }

        return self
