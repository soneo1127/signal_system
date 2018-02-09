import numpy as np
import matplotlib.pyplot as plt
 
x = np.array([9.0, 10.5, 10.6, 10.4, 11.1, 11.3, 9.7, 9.8, 10.3, 10.0, 9.8, 10.5, 10.2, 9.6, 9.9,
 10.2, 10.6, 8.3, 9.9, 8.7, 9.8, 10.3, 7.9, 9.9, 10.8, 10.1, 10.1, 11.9, 8.5, 9.1, 10.2, 9.8, 9.7,
 11.4, 9.7, 8.8])


# ビンを指定 
bins = np.array([8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0])
# ヒストグラムを出力
fig = plt.figure()
plt.hist(x, bins=bins)
fig.show()

plt.savefig("hist_b.png")