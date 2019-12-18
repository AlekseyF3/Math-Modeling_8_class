import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
t = np.arange(0,10,0.1)
def inv(n,t):
    dndt = -k*n*t
    return dndt
k = 0.05
n_0 = 1000
invest = odeint(inv, n_0,t)
plt.plot(t,invest, label = "iii")
plt.xlabel("--------")
plt.ylabel("зззззз")
plt.title("инвестиции")
plt.show()
