#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
font_paths = mpl.font_manager.findSystemFonts()
plt.rcParams['font.family'] = 'Kozuka Mincho Pr6N'#日本語フォント設定

T = 1 / 6.0

X = [3.0, 2.0, 0.0, -1.0, 1.0, 3.0, 2.0, -1.0]

Y_2=[]

for i in range(2, 6):
	Y_2.append( -( 1 / ( 6 * T ) ) * X[ i - 2 ] - ( 1 / ( 6 * T ) ) * X[ i - 1 ] + ( 1 / ( 6 * T ) ) * X[ i + 1 ] + ( 1 / ( 6 * T ) ) * X[ i + 2 ] )

n_2 = [2, 3, 4, 5]

print(Y_2)

plt.scatter(n_2, Y_2, c="b", marker='o', label="y2(n)")

plt.title('低域微分処理')
#グラフの軸
plt.xlabel('n')
plt.ylabel('y(n)')

plt.xlim(0, 7)
plt.ylim(-15, 15)
plt.savefig('3-4.png')
plt.legend()

plt.show()