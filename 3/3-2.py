#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
font_paths = mpl.font_manager.findSystemFonts()
plt.rcParams['font.family'] = 'Kozuka Mincho Pr6N'#日本語フォント設定

T = 1 / 6.0

X = [3.0, 2.0, 0.0, -1.0, 1.0, 3.0, 2.0, -1.0]

Y_2=[]

for i in range(1, 7):
	Y_1.append( -( 1 / ( 2 * T ) ) * X[ i - 1 ] + ( 1 / ( 2 * T ) ) * X[ i + 1 ] )

n_1 = [1, 2, 3, 4, 5, 6]

print(Y_1)

plt.scatter(n_1, Y_1, c="b", marker='o', label="y(n)")

plt.title('(3-4)の微分処理')
#グラフの軸
plt.xlabel('k')
plt.ylabel('x(k), y(k)')

plt.xlim(0, 7)
plt.ylim(-15, 15)
plt.savefig('3-2.png')
plt.legend()

plt.show()