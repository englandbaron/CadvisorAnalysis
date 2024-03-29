#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019-07-15 21:21
"""

from ToolUtils.PublicUtils import LOG,JsonParser
from ToolUtils import FuncHttpMethod
from CadvisorModel.Resource import MachinestatModel , ContainerModel , ContainerSummaryModel


class AnalysisEngine(object):
    def __init__(self,ResourceType,Field):
        self.ResourceType = ResourceType
        self.Field = Field

        if self.ResourceType == "FILE":
            self.Resource = self.GetResourceByFILE(self.Field)
        if self.ResourceType == "HTTP":
            self.Resource = self.GetResourceByHTTP(self.Field)

    def GetMachineCapacity(self):
        LOG.debug("GetMachineCapacity: %s" % self.Field)
        if self.ResourceType == "FILE":
            return self.GetResourceByFILE("%s" % self.Field)["memory_capacity"]
        if self.ResourceType == "HTTP":
            return self.GetResourceByHTTP("%s" % self.Field)["memory_capacity"]

    def MachineAnalysis(self):
        return MachinestatModel(self.Resource).INIT()

    def ContainerSetAnalysis(self):
        return ContainerModel(self.Resource).INIT()

    def ContainerSummaryAnalysis(self):
        return ContainerSummaryModel(self.Resource).INIT()

    @staticmethod
    def GetResourceByFILE(Field):
        FILE = open(Field)
        FILE_READ = FILE.read()
        return JsonParser.JsonToObj(FILE_READ)

    @staticmethod
    def GetResourceByHTTP(Field):
        class BasicGetRequest:
            @FuncHttpMethod.GET(url=Field,auth=None,verify=False)
            def GetResult(response):
                return JsonParser.JsonToObj(response.text)
        return BasicGetRequest.GetResult()