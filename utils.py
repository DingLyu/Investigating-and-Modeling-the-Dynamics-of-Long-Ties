# /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ding lyu
@email: dylan_lyu@sjtu.edu.cn
"""

import csv
import time
import torch
import math as mt
import numpy as np
import scipy as sp
import pandas as pd
import networkx as nx
import seaborn as sns
import torch.nn as nn
import matplotlib.pyplot as plt

def read(filename):
    Data = []
    with open(filename, 'r') as f:
        for data in f.readlines():
            Data.append(data.strip('\n').split(' '))
    f.close()
    return Data

def write(filename, Data):
    with open(filename, 'w') as f:
        for data in Data:
            for d in data[:-1]:
                f.write(d)
                f.write(' ')
            f.write(data[-1])
            f.write('\n')
    f.close()

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), sp.stats.sem(a)
    h = se * sp.stats.t.ppf((1 + confidence) / 2., n - 1)
    return h

def read_endowments(file):
    endowments = dict()
    with open(file) as f:
        for line in csv.reader(f):
            endowment = line[1:]
            endowment = list(map(float, endowment))
            endowments[line[0]] = np.array(endowment)

    f.close()
    return endowments
