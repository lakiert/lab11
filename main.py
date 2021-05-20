import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import *
from matplotlib import cm

# zad1

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
#
# z = np.linspace(0, 2 * np.pi)
# x = np.sin(z)
# y = 2 * np.cos(z)
#
# ax.plot(z, x, y)
# plt.show()

# zad2

# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# def randrange(n, vmin, vmax):
#     return (vmax-vmin)*np.random.rand(n)+vmin
#
# for c, m in [('r', 'o'), ('b', '*'), ('g', 'P'), ('m','^'), ('y','s')]:
#     s1 = randrange(100, 20, 30)
#     s2 = randrange(100, 30, 40)
#     s3 = randrange(100, 40, 50)
#     s4 = randrange(100, 50, 60)
#     s5 = randrange(100, 60, 70)
#     ax.scatter(s1, s2, s3, s4, s5, c=c, marker=m)
#
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# plt.show()

#zad3

# fig = plt.figure(figsize=(16,9))
# ax = fig.add_subplot(1,3,1, projection='3d')
#
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, cmap=cm.hot, linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf,shrink=0.5, aspect=10, orientation='vertical', pad=0.1)
#
# ax = fig.add_subplot(1,3,2, projection='3d')
# surf1 = ax.plot_surface(X, Y, Z, cmap=cm.Pastel1, linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf1,shrink=0.5, aspect=10, orientation='vertical', pad=0.1)
#
# ax = fig.add_subplot(1,3,3, projection='3d')
# surf1 = ax.plot_surface(X, Y, Z, cmap=cm.ocean, linewidth=1, antialiased=False)
# ax.set_zlim(-1.01, 1.01)
# fig.colorbar(surf1,shrink=0.5, aspect=10, orientation='vertical', pad=0.1)
#
# plt.show()
