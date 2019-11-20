import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos
from matplotlib.animation import FuncAnimation

R = 1
fig, ax = plt.subplots()

xmm, = plt.plot([], [], 'o')

xdata,ydata=[],[]

ax.set_xlim(-5, 15)

ax.set_ylim(-5,5)

def gm(t):
    xdata.append(R*(t-sin(t)))
    ydata.append(R*(1-cos(t)))
    xmm.set_data(xdata,ydata)

ani = FuncAnimation(fig,
                    gm,
                    frames = np.arange(0,4*np.pi,0.1),
                    interval = 30)
ani.save('xren.gif')