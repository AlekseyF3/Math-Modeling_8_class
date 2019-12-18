import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
t = np.arange(0,10, 0.1)
def bakt(x,t):
    dxdt = k*x
    return dxdt
k = 0.5
x_0 = 5

solve_b = odeint(bakt, x_0,t)
plt.plot(t, solve_b[:,0], label = "Размножение бактерий")
plt.xlabel("Скорость")
plt.ylabel("Функция")
plt.title("Размножение бактерий")
plt.show()

