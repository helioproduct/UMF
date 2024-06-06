import numpy as np
import matplotlib.pyplot as plt

# Parameters
l = 1.0  # Length of the string
T = 10.0  # Total time
a = 1.0  # Wave speed
N = 100  # Number of spatial steps
M = 1000  # Number of time steps

# Discretization
dx = l / N
dt = T / M
x = np.linspace(0, l, N + 1)
t = np.linspace(0, T, M + 1)

# Stability condition
CFL = a * dt / dx
if CFL > 1:
    raise ValueError("CFL condition is not satisfied")

# Initialize the solution array
u = np.zeros((N + 1, M + 1))

# Initial conditions
u[:, 0] = 0
u[:, 1] = 0

# Boundary conditions
for j in range(1, M + 1):
    u[0, j] = np.sin(t[j])

# Time stepping
for j in range(1, M):
    for i in range(1, N):
        u[i, j + 1] = (
            2 * u[i, j]
            - u[i, j - 1]
            + CFL**2 * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j])
        )
    # Neumann boundary condition at x = l
    u[N, j + 1] = u[N - 1, j + 1]

# Plot the solution at different time steps
plt.figure(figsize=(10, 6))
for j in range(0, M + 1, M // 10):
    plt.plot(x / 100, u[:, j], label=f"t={t[j]:.2f}")
plt.xlabel("x")
plt.ylabel("u(x,t)")
plt.title("Задание 2")
plt.legend()
plt.grid(True)
plt.show()
