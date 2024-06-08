import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

l1 = 1
l2 = 1

x = np.linspace(0, l1, 100)
y = np.linspace(0, l2, 100)
X, Y = np.meshgrid(x, y)

U = (l1 / np.pi) * np.sin(np.pi * X / l1) * np.sinh(np.pi * Y / l1)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, U, cmap="viridis")

ax.set_title("Solution of Laplace Equation")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("u(x, y)")

plt.show()
