#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

x = np.array([0.0, 3.0, 4.0, 1.0, 2.0, -1.0, 0.0, 10, -1.0, 0.0])
N = 10 # リストの大きさ

µ_n = np.sum(x) / N

σ_n_2 =  np.sum( np.power(x-µ_n, 2) ) / (N-1) # 分散 

σ_n = np.sqrt(σ_n_2)

print('xの分散は{}'.format(σ_n_2))
print('xの標準偏差は{}'.format(σ_n))

