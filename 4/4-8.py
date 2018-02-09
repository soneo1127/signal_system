#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

x = np.array([1, 1, 1, 1, 0, 0, 0, 0])
N = 8 # リストの大きさ

E_x = np.sum(np.power(x, 2)) # エネルギー

P_x =  E_x / N # 平均パワー

print('xの平均パワーは{}'.format(P_x))

A_x = np.sqrt(P_x)

print('xの実効値は{}'.format(A_x))

