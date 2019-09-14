#!/usr/bin/env python
# encoding: utf-8

"""
@author: Tang Smith
@contact: 415107188@qq.com
@software: PyCharm
@time: 2019/9/14 下午12:32
"""
from random import random
import numpy as np
import matplotlib.pyplot as plt

# Key values
xmin = 0
xmax = 10
scale = 10.0
seed = 10

np.random.seed = seed
x = np.linspace(xmin, xmax, num=1000)

from random import seed
from random import random
from matplotlib import pyplot

seed(1)

random_walk = list()
random_walk.append(0)

def CheckValueLegal(value):
    if value > 0 and value < 100:
        return True
    return False

def GenerateRandomValue(value):
    movement = -1 if random() < 0.5 else 1
    result = value + movement
    if CheckValueLegal(result):
        return result
    else:
        return GenerateRandomValue(value)

for i in range(1, 10000):
    value = GenerateRandomValue(random_walk[i-1])
    random_walk.append(value)

pyplot.plot(random_walk)
pyplot.show()