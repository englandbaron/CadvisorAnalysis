#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019/9/13 下午8:57
"""

from .UtilizationModel import UtilizationModel

"""
Random MIP Generator Rule:
"""
class UtilizationModelStochastic(UtilizationModel):
    def __init__(self,**kwargs):
        """
        :param kwargs: seed -> Host
        """
        # TODO: Model Initial Func
        super().__init__(kwargs)
        self.seed = kwargs.get("seed")
        self.utilization = 0.0

    def MIPGenerator(self):
        self.RandomMIPGenerator(self.seed)

    def RandomMIPGenerator(self, seed):
        # TODO: Random Agorithm
        pass

    def getUtilization(self):
        return self.utilization