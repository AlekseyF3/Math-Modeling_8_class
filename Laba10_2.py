import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

t = np.arange(0, 20, 0.01)
g = 9.8
k = 2
def diff_func(z,t):
    s, v = z
    ds_dt = v
    dv_dt = -g*np.sin(s/l) - k/m *v
    return ds_dt,dv_dt

l = 5
m = 10
s0 = 1
v0 = 1
z0 = s0,v0

sol = odeint(diff_func,z0,t)
plt.plot(t,sol[:,0], 'b')

    