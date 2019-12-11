import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from numpy import cos, sin
a = 5
b = 4
c = 7
fig  = plt.figure()
def circle_func(x_c_p,
                y_c_p,
                R,
                N):
    x = np.linspace(-5,5,100)
    y = a*x**2 + x+c
    for i in range (0,2,1):
        alpha = np.linespace(0,2*np.pi,N)
        x[i] = x_c_p + R*np.cos(alpha)
        y[i] = y_c_p + R*np.sin(alpha)
        return x,y
    
z = np.linspace(0.4*np.pi,100)
R = 1
x_c_m = R*t
anim_list = []
N = 100
for i in range(0,100,1):
    x,y = circle_func(x_c_m[i],R,R=R,N=N)
    circle, = plt.plot(x,y,"g-",lw = 2)
    cic, = plt.plot(cycl_x[:i], cycl_y[:i], "r-", lw =2)
    anim_object, = plt.plot(x[:i],y[:i], "-", color = 'y')
    point, = plt.plot(x[i], y[i], 'o')
    anim_list.append([circle, cic,point])
plt.axis("equal")
ani = ArtistAnimation(fig,anim_list, interval = 55)
ani.save("crazy_danila.gif")
    