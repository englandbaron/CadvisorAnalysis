#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: zzetian@cn.ibm.com
@software: PyCharm
@time: 2019-08-02 19:17
"""
from __future__ import division
# import dateutil.parser
# from datetime import datetime

from CadvisorModel.ProjectWorkspace import ProjectWorkspace
from ToolUtils import JsonParser,LOG

# workspace = ProjectWorkspace("HTTP", "http://node1:8080")
workspace = ProjectWorkspace("FILE","2019_08_07_20_26_03/")
MachineStatParser = workspace.MachineStatParser()

for Info in MachineStatParser.CollectList:
    LOG.success("Time: %s | CpuUsage: %s " % (Info['time'],Info['cpu_usage']))
    # JsonParser.BeautifulOutput(Info)
    LOG.success("================================================")