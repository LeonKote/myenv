import matplotlib.pyplot as plt
import numpy as np

# Генерируем значения x от -2π до 2π
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Вычисляем значения функции sin(x) + cos(x)
y = np.sin(x) + np.cos(x)

# Создаем график
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$\sin(x) \times \cos(x)$', color='b')
plt.title('График функции $\\sin(x) \\times \\cos(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
