import numpy as np
import matplotlib.pyplot as plt
 
N = 64

x = np.random.uniform(-1, 1, N)

fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10,4))

axL.set_xlabel("n")
axL.set_ylabel("degree")
axL.plot(x, 'o')

# ヒストグラムを出力
axR.hist(x)

fig.show()
fig.savefig("4_10_a.png")