import numpy as np
import matplotlib
matplotlib.use('Agg')  # Використовуємо Agg backend для Python 3.13
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x**2

a, b = 0, 2

quad_result, quad_error = spi.quad(f, a, b)
print(f"Аналітичний (quad) інтеграл: {quad_result:.6f}, похибка: {quad_error:.2e}")

N = 100000
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
monte_carlo_result = (b - a) * np.mean(y_rand)
print(f"Метод Монте-Карло: {monte_carlo_result:.6f}, при N={N}")

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f"Інтеграл f(x)=x² від {a} до {b}")
plt.grid()
plt.savefig('graph.png', dpi=300, bbox_inches='tight')
print(f"\nГрафік збережено у файл 'graph.png'")