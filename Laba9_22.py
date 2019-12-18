import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
t = np.arange(0,100,0.1)
def inv(v,t):
    dvdt = (F-k*v**2)/m
    return dvdt
k = 0.05
m = 15
v_0 = 0
F = 50

sila = odeint(inv, v_0,t)
plt.plot(t,sila, label = "iii")
plt.xlabel("--------")
plt.ylabel("зззззз")
plt.title("закон")
plt.show()