import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return x**2

a = 0
b = 2

N = 100000  
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, f(b), N)

under_curve = y_rand < f(x_rand)

rect_area = (b - a) * f(b)

monte_carlo_integral = rect_area * np.sum(under_curve) / N

quad_result, error = spi.quad(f, a, b)

print(f"Інтеграл методом Монте-Карло: {monte_carlo_integral}")
print(f"Інтеграл методом quad: {quad_result}, помилка: {error}")
x_vals = np.linspace(a, b, 100)
y_vals = f(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, 'r', linewidth=2, label='$f(x) = x^2$')
plt.fill_between(x_vals, y_vals, alpha=0.3, color='gray')
plt.scatter(x_rand, y_rand, c=under_curve, cmap='coolwarm', s=1, alpha=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод Монте-Карло для обчислення інтегралу')
plt.legend()
plt.grid()
plt.show()
