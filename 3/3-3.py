#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
font_paths = mpl.font_manager.findSystemFonts()
plt.rcParams['font.family'] = 'Kozuka Mincho Pr6N'#日本語フォント設定

T = 1 / 6.0

X = [3.0, 2.0, 0.0, -1.0, 1.0, 3.0, 2.0, -1.0]

Y_4_1=[]

for i in range(1, 9):
	s = 0
	for k in range(i):
		s = s + X[k]
	Y_4_1.append( T * s )

n_4_1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(Y_4_1)

plt.scatter(n_4_1, Y_4_1, c="b", marker='o', label="y(n)")

plt.title('完全積分処理')
#グラフの軸
plt.xlabel('n')
plt.ylabel('y(n)')

plt.xlim(0, 9)
plt.ylim(0, 2)
plt.savefig('3-3_1.png')
plt.legend()

plt.show()

M_i = 3
L = int( (M_i-1)/2 )

Y_4_2=[]

for i in range(1, 7):
	s = 0
	for k in range(i-L, i+L+1):
		s = s + X[k]
	Y_4_2.append( T * s )

n_4_2 = [2, 3, 4, 5, 6, 7]

print(Y_4_2)

plt.scatter(n_4_2, Y_4_2, c="b", marker='o', label="y(n)")

plt.title('区間積分処理')
#グラフの軸
plt.xlabel('n')
plt.ylabel('y(n)')

plt.xlim(0, 9)
plt.ylim(0, 2)
plt.savefig('3-3_2.png')
plt.legend()

plt.show()