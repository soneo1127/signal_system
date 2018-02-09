# 5-5.py
# 使用言語 python3

import matplotlib.pyplot as plt

# サンプルデータの定義 ========================================================
N = 5         # Signal length
x = [1, 0, 1, 0, 0]
# 自己相関関数
Rr = [0,0,0,0,0]
def auto_correlate(x):
	for m in range(N-1):
		for n in range(N-1):
			if(n+m) >= N:
				break
			Rr[m] += x[n] * x[n+m]
		Rr[m] = Rr[m] / (N-m)
	return Rr

Rr = auto_correlate(x)
plt.plot(Rr)
plt.title("5-5.py")
plt.savefig("5-5.png")