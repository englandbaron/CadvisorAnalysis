#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-07-15 21:20
"""

from ToolUtils import LOG, JsonParser

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
            self.Field = self.Field + "/" if self.Field[-1] != '/' else self.Field
            LOG.debug(self.Field)
            self.Memory = AnalysisEngine(self.ResourceType,'%sapi/v2.1/machine?recursive=true' % self.Field).GetMachineCapacity()
        if ResourceType != "FILE" and ResourceType != "HTTP":
            LOG.error("Resource Is Invalid!!!Exiting...")
            exit(0)
        LOG.debug("The Memory Capacity: %s" % self.Memory)

    def MachineStatParser(self):
        """
        dataset/machinestats.json
        :return: Machinestat Model
        """
        MachineAnalysisEngine = AnalysisEngine(self.ResourceType,"%smachinestats.json" % self.Field if self.ResourceType == "FILE" else "%sapi/v2.1/machinestats?recursive=true" % self.Field).MachineAnalysis()
        return MachineAnalysisEngine


    def ContainerStatParser(self):
        """
        Input: dataset/stats.json
        :return: Stats Model
        """
        ContainerSetAnalysisEngine = AnalysisEngine(self.ResourceType,"%sstats.json" % self.Field if self.ResourceType == "FILE" else "%sapi/v2.1/stats?recursive=true" % self.Field).ContainerSetAnalysis()
        return ContainerSetAnalysisEngine


    def SummaryStatParser(self):
        """
        Input: dataset/summary.json
        :return: Summary Model
        """
        ContainerSummaryAnalysisEngine = AnalysisEngine(self.ResourceType,"%ssummary.json" % self.Field if self.ResourceType == "FILE" else "%sapi/v2.1/summary?recursive=true" % self.Field).ContainerSummaryAnalysis()
        return ContainerSummaryAnalysisEngine

