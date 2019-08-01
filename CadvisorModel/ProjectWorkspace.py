#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-07-15 21:20
"""

from ToolUtils.PublicUtils import LOG
from CadvisorModel.AnalysisEngine import AnalysisEngine

class ProjectWorkspace(object):
    ###
    #
    # ResourceType:
    # FILE
    # HTTP
    ###
    # Field:
    # attributes,
    # machinestats,
    # spec,
    # stats
    # summary
    ###
    def __init__(self, ResourceType=None, Field=None):
        self.ResourceType = ResourceType
        self.Field = Field
        if ResourceType is None or Field is None:
            LOG.error("Field Is Not Specificed!!!")
            exit(0)
        if ResourceType == "FILE":
            LOG.debug("ResourceType is FILE")
            self.Memory = AnalysisEngine(self.ResourceType,"%smachine.json" % self.Field).GetMachineCapacity()
        if ResourceType == "HTTP":
            LOG.debug("ResourceType is HTTP")
            # self.Memory =
        LOG.success("The Memory Capacity: %s" % self.Memory)

    def MachineStatParser(self):
        """
        dataset/machinestats.json
        :return: Machinestat Model
        """
        MachineAnalysisEngine = AnalysisEngine(self.ResourceType,"%smachinestats.json" % self.Field).MachineAnalysis()
        return MachineAnalysisEngine


    def ContainerStatParser(self):
        """
        Input: dataset/stats.json
        :return: Stats Model
        """
        ContainerSetAnalysisEngine = AnalysisEngine(self.ResourceType,"%sstats.json" % self.Field).ContainerSetAnalysis()
        return ContainerSetAnalysisEngine


    def SummaryStatParser(self):
        """
        Input: dataset/summary.json
        :return: Summary Model
        """
        ContainerSummaryAnalysisEngine = AnalysisEngine(self.ResourceType,"%ssummary.json" % self.Field).ContainerSummaryAnalysis()
        return ContainerSummaryAnalysisEngine
