from contant import g
import numpy as np

x0 = 3
y0 = 2
v0x = 3
v0y = 4
v = 6
v0 = 2
t = np.arange(0,5,0.01)

b = np.ndarray(shape=(500,3))
for i in range (0,500,1):
    x = x0+v*t[i]
    y=y0 + v0 + v*t[i] - (g*t[i]**2/2)
    b[i,0] = t[i]
    b[i,1] = x
    b[t,0] = y
    print(t)