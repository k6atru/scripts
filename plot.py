#!/usr/bin/env python3
#%%
# import os
# import sys
# homedir = os.environ['HOME']
# #os.path.joinの2つめの引数には/をつけない
# pipdir = os.path.join(homedir, ".local/lib/python3.6/site-packages")
# sys.path.append(pipdir)

#%%
import numpy as np
import matplotlib.pyplot as plt
# 4dist.txtを読み込んでグラフに出力する
data = np.loadtxt('dihed.txt')
#背景白
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111)
#縦軸の範囲を指定
ax.set_ylim(0, 360)
ax.plot(data[:,0]*0.5, data[:,1])
ax.set_xlabel('Time (ns)')
ax.set_ylabel('Dihedral angle (degree)')
fig.show()
fig.savefig("dihed.png", dpi=500)


# %%
print()