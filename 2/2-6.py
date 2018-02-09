#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
font_paths = mpl.font_manager.findSystemFonts()
plt.rcParams['font.family'] = 'Kozuka Mincho Pr6N'#日本語フォント設定

X_0 = [0,0,0,0]
Y_0 = [0.05, -0.52, 0.05, 0.08]

X_1 = [1,1,1,1]
Y_1 = [0.81, 1.28, 0.85, 1.01]

X_2 = [2,2,2,2]
Y_2 = [0.97, 0.83, 0.89, 0.65]

X_3 = [3,3,3,3]
Y_3 = [0.61, 0.43, 0.55, 0.56]

X_4 = [4,4,4,4]
Y_4 = [0.34, 0.16, 0.25, -0.07]

X_5 = [5,5,5,5]
Y_5 = [-0.24, 0.06, 0.13, -0.15]

X_list = X_0 + X_1 + X_2 + X_3 + X_4 + X_5
Y_list = Y_0 + Y_1 + Y_2 + Y_3 + Y_4 + Y_5

#plt.scatter(X_list, Y_list, c="b", marker='o', label="加算平均前")

ave_X_0 =  [sum(X_0) / len(X_0)]
ave_Y_0 =  [sum(Y_0) / len(Y_0)]

ave_X_1 =  [sum(X_1) / len(X_1)]
ave_Y_1 =  [sum(Y_1) / len(Y_1)]

ave_X_2 =  [sum(X_2) / len(X_2)]
ave_Y_2 =  [sum(Y_2) / len(Y_2)]

ave_X_3 =  [sum(X_3) / len(X_3)]
ave_Y_3 =  [sum(Y_3) / len(Y_3)]

ave_X_4 =  [sum(X_4) / len(X_4)]
ave_Y_4 =  [sum(Y_4) / len(Y_4)]

ave_X_5 =  [sum(X_5) / len(X_5)]
ave_Y_5 =  [sum(Y_5) / len(Y_5)]

ave_X_list = ave_X_0 + ave_X_1 + ave_X_2 + ave_X_3 + ave_X_4 + ave_X_5
ave_Y_list = ave_Y_0 + ave_Y_1 + ave_Y_2 + ave_Y_3 + ave_Y_4 + ave_Y_5

plt.scatter(ave_X_list, ave_Y_list, c="r", marker='x', label="MA処理前")

MA_X_1 = [sum(ave_X_0 + ave_X_1 + ave_X_2) / 3]
MA_Y_1 = [sum(ave_Y_0 + ave_Y_1 + ave_Y_2) / 3]

MA_X_2 = [sum(ave_X_1 + ave_X_2 + ave_X_3) / 3]
MA_Y_2 = [sum(ave_Y_1 + ave_Y_2 + ave_Y_3) / 3]

MA_X_3 = [sum(ave_X_2 + ave_X_3 + ave_X_4) / 3]
MA_Y_3 = [sum(ave_Y_2 + ave_Y_3 + ave_Y_4) / 3]

MA_X_4 = [sum(ave_X_3 + ave_X_4 + ave_X_5) / 3]
MA_Y_4 = [sum(ave_Y_3 + ave_Y_4 + ave_Y_5) / 3]

MA_X_list = MA_X_1 + MA_X_2 + MA_X_3 + MA_X_4
MA_Y_list = MA_Y_1 + MA_Y_2 + MA_Y_3 + MA_Y_4

print(MA_X_1)
print(MA_Y_list)

plt.scatter(MA_X_list, MA_Y_list, c="b", marker='+', label="MA処理後")


plt.title('移動平均前と移動平均後の結果')
#グラフの軸
plt.xlabel('k')
plt.ylabel('x(k), y(k)')

plt.xlim(0, 5)
plt.ylim(-1.5, 1.5)
plt.savefig('2-6.png')
plt.legend()

plt.show()