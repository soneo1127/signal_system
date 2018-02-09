# 5-6.py
# 使用言語 python3

import numpy as np
import matplotlib.pyplot as plt


# サンプルデータの定義 ========================================================
N = 16         # Signal length
y = np.array([0,0,0,0,0.1,0.42,0.72,0.58,0,-0.58,-0.72,-0.42,-0.10,0,0,0])
x1 = np.array([0,0.1,0.42,0.72,0.58,0,-0.58,-0.72,-0.42,-0.10,0,0,0,0,0,0])
x2 = x1 + 0.7
x3 = x1 * 1.5
# 自己相関関数
Rr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

def cross_covariance(x, y):
	µ_x = np.average(x)
	µ_y = np.average(y)
	for m in range(-N+1, N-1):
		for n in range(N-1):
			if(n+m) < 0:
				continue
			if(n+m) >= N:
				break
			Rr[m] += (x[n] - µ_x) * (y[n+m] - µ_y)
		Rr[m] = Rr[m] / (N-abs(m))
	return Rr

# 標準偏差	

def cross_corelation(x, y):
	σ_x = np.std(x)
	σ_y = np.std(y)
	µ_x = np.average(x)
	µ_y = np.average(y)
	for m in range(-N+1, N-1):
		for n in range(N-1):
			if(n+m) < 0:
				continue
			if(n+m) >= N:
				break
			Rr[m] += (x[n] - µ_x) * (y[n+m] - µ_y)
		Rr[m] = Rr[m] / (N-abs(m))
		Rr[m] = Rr[m] / (σ_x * σ_y)
	return Rr

plt.figure()
Rr = correlate(y, x1)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x1 correlation")
plt.savefig("5-7-y-x1-correlation.png")

plt.figure()
Rr = cross_covariance(y, x1)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x1 cross_covariance")
plt.savefig("5-7-y-x1-cross_covariance.png")

plt.figure()
Rr = cross_corelation(y, x1)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x1 cross_corelation")
plt.savefig("5-7-y-x1-cross_corelation.png")

plt.figure()
Rr = correlate(y, x2)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x2 correlation")
plt.savefig("5-7-y-x2-correlation.png")

plt.figure()
Rr = cross_covariance(y, x2)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x2 cross_covariance")
plt.savefig("5-7-y-x2-cross_covariance.png")

plt.figure()
Rr = cross_corelation(y, x2)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x2 cross_corelation")
plt.savefig("5-7-y-x2-cross_corelation.png")

plt.figure()
Rr = correlate(y, x3)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x3 correlation")
plt.savefig("5-7-y-x3-correlation.png")

plt.figure()
Rr = cross_covariance(y, x3)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x3 cross_covariance")
plt.savefig("5-7-y-x3-cross_covariance.png")

plt.figure()
Rr = cross_corelation(y, x3)
Rr = np.roll(Rr, N)
plt.plot(Rr)
plt.title("5-7, y, x3 cross_corelation")
plt.savefig("5-7-y-x3-cross_corelation.png")