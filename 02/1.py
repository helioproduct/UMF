import numpy as np
import matplotlib.pyplot as plt

l = 1.0
T = 10.0
a = 1.0
N = 100
M = 1000

# Discretization
dx = l / N
dt = T / M
x = np.linspace(0, l, N + 1)
t = np.linspace(0, T, M + 1)

CFL = a * dt / dx
if CFL > 1:
    raise ValueError("CFL condition is not satisfied")

u = np.zeros((N + 1, M + 1))

u[:, 0] = 0
u[:, 1] = 0

for j in range(1, M + 1):
    u[0, j] = np.sin(t[j])

for j in range(1, M):
    for i in range(1, N):
        u[i, j + 1] = (
            2 * u[i, j]
            - u[i, j - 1]
            + CFL**2 * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j])
        )
    u[N, j + 1] = u[N - 1, j + 1]


l = 1.0
T = 10.0
a = 1.0
M = 1000

dx = l / N
dt = T / M
x = np.linspace(0, l, N + 1)
t = np.linspace(0, T, M + 1)

CFL = a * dt / dx
if CFL > 1:
    raise ValueError("CFL condition is not satisfied")

u = np.zeros((N + 1, M + 1))

u[:, 0] = 0
u[:, 1] = 0

for j in range(1, M + 1):
    u[0, j] = np.sin(t[j])

for j in range(1, M):
    for i in range(1, N):
        u[i, j + 1] = (
            2 * u[i, j]
            - u[i, j - 1]
            + CFL**2 * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j])
        )
    u[N, j + 1] = u[N - 1, j + 1]

x_indices = [0, N // 4, N // 2, 3 * N // 4, N]
x_values = x[x_indices]

plt.figure(figsize=(12, 8))
for i, xi in enumerate(x_indices):
    plt.plot(t, u[xi, :], label=f"x={x_values[i] / 100:.2f}")

plt.xlabel("t")
plt.ylabel("u(x,t)")
plt.title("Задание 2")
plt.legend()
plt.grid(True)
plt.show()
