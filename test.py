#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-07-15 21:15
"""
from ToolUtils.PublicUtils import LOG
from CadvisorModel.ProjectWorkspace import ProjectWorkspace

workspace = ProjectWorkspace("FILE","DataSet-Demo/")
LOG.success("MachineStats: %s" % workspace.MachineStatParser())
LOG.success("ContainerStats: %s" % workspace.ContainerStatParser())
LOG.success("ContainerStats: %s" % workspace.SummaryStatParser())