#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019年 09月 13日 星期五 00:10:45 CST
"""

from .Predicate import Predicate

class CheckNodeMemoryPressurePredicate(Predicate):
    """
    Algorithm: Document/SchedulerStudy.md/CheckNodeConditionPredicate
    """
    def __init__(self, pod):
        # TODO:
        super().__init__(pod)

    def JobRunnerInterface(self):
        super().JobRunnerInterface()