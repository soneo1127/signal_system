# 5-6.py
# 使用言語 python3

import numpy as np
import matplotlib.pyplot as plt


# サンプルデータの定義 ========================================================
N = 4         # Signal length
x = [0,1,-1,0]
y = [1,1,1,-1]
# 自己相関関数
Rr = [0,0,0,0,0,0,0]
def correlate(x, y):
	for m in range(-N+1, N-1):
		for n in range(N-1):
			if(n+m) < 0:
				continue
			if(n+m) >= N:
				break
			Rr[m] += x[n] * y[n+m]
		Rr[m] = Rr[m] / (N-abs(m))
	return Rr

Rr = correlate(x, y)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-6.py")
plt.savefig("5-6.png")