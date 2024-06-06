import numpy as np
import matplotlib.pyplot as plt

length = 0.1
constant_a = 10**3
constant_a2 = 10**6
multiplier = constant_a**2 * length**2
wave_number = 0.2**0.5 / constant_a
psinus = 1 / np.sin(wave_number * length)


def series(x, t):
    result = (
        500 * np.sin(wave_number * (x - length)) * psinus
        - 600 * np.sin(wave_number * x) * psinus
    )
    N = 100
    for n in range(1, N, 1):
        sign = -1
        lambda_n = np.pi * length / n
        denominator = (constant_a * np.pi * n) ** 2 - 0.8 * length**2

        coefficient = multiplier * n / denominator
        term_coefficient = (
            500 * length * coefficient * 0.8**0.5
            + 600 * coefficient * constant_a * np.pi * n * (-1) ** n
            - 700 / (np.pi * n)
        )
        additional_term = (
            term_coefficient
            * np.exp(-(lambda_n**2) * t - 0.2 * t)
            * np.sin(lambda_n * x)
        )
        result += additional_term
        sign *= -1
    return result


x_values = np.arange(0, length, 0.01)
t_values = np.arange(0, 10, 0.1)

xdata = []
ydata = []
zdata = []

for x in x_values:
    for t in t_values:
        xdata.append(x)
        ydata.append(t)
        zdata.append(1000 + series(x, t))

xdata = np.array(xdata)
ydata = np.array(ydata)
zdata = np.array(zdata)

fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection="3d")
ax.plot_trisurf(ydata, xdata, zdata, cmap="YlOrBr")
ax.set_xlabel("T")
ax.set_ylabel("X")
ax.set_zlabel("U")

plt.show()
