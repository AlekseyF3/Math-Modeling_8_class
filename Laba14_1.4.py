import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0.7,2*np.pi,100)
theta = np.linspace(0.7,np.pi,100)

l = 7
m = 5
n = 4

x = np.outer(phi, np.cos(theta)) + np.outer(l,theta**2)
y = np.outer(phi, np.sin(theta)) + np.outer(m, theta**2)
z = n* np.outer(np.ones(np.size(phi)),np.ones(np.size(theta)))

ax.plot_surface(x,y,z, color = "g")
plt.show()