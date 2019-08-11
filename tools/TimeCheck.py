#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-08-07 21:40
"""
from __future__ import division
import os
import sys
import dateutil.parser
from datetime import datetime

from CadvisorModel.ProjectWorkspace import ProjectWorkspace
from ToolUtils import JsonParser,LOG,BASE_DIR

FolderList = [folder for folder in os.listdir(BASE_DIR) if "2019_" in folder]
for Folder in FolderList:
    workspace = ProjectWorkspace("FILE", "%s/%s/" % (BASE_DIR,Folder))
    MachineStatParser = workspace.MachineStatParser()
    ContainerStatParser = workspace.ContainerStatParser()

    machine_max_value = float(0)
    machine_min_value = float(2**100)
    for mos in range(1, len(MachineStatParser.CollectList)):
        cur_time = float(datetime.timestamp(dateutil.parser.parse(MachineStatParser.CollectList[mos]['time'])) * 1000)
        LOG.success(cur_time)
        machine_max_value = max(machine_max_value,cur_time)
        machine_min_value = min(machine_min_value,cur_time)
    LOG.success("Machine Stat:")
    LOG.success("MIN Value: %s" % machine_min_value)
    LOG.success("MAX Value: %s" % machine_max_value)
    LOG.success("=====================================================================")

    container_max_value = float(0)
    container_min_value = float(2 ** 100)
    for mos in range(1, len(ContainerStatParser.CollectList)):
        for time in [datetime.timestamp(dateutil.parser.parse(t['time'])) * 1000 for t in ContainerStatParser.CollectList[mos]['STATS']]:
            LOG.success(time)
            container_max_value = max(container_max_value,float(time))
            container_min_value = min(container_min_value,float(time))
    LOG.success("Container Stat:")
    LOG.success("MIN Value: %s" % container_min_value)
    LOG.success("MAX Value: %s" % container_max_value)
    LOG.success("=====================================================================")