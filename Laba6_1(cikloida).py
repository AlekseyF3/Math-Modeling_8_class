import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos
t = np.arange(-2*np.pi,2*np.pi,0.1)
R = 3
x = R*(t - sin(t))
y = R*(1 - cos(t))
plt.plot(x,y,linestyle = '--', linewidth = 5)
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.axis('equal')
plt.show()