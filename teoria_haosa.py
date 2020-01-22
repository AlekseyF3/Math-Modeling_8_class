import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

t = np.arange(0, 200, 0.01)

def diff_func(z,t):
    x, y = z
    dx_dt = y
    dy_dt = u*(1-x**2) * y - x
    return dx_dt, dy_dt
x0 = 15
y0 = 10
z0 = x0, y0

u = 1


sol = odeint(diff_func,z0,t)
plt.plot(sol[:,0],sol[:,1], 'b')