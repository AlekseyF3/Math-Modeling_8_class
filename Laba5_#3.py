import matplotlib.pyplot as plt
import numpy as np
def ell_circl_plotter(R = 2,a = 2,b = 1, title = 'circl.plotter'):
    x = np.arange(-4,4,0.01)
    y = np.arange(-2,2,0.01)
    X,Y = np.meshgrid(x,y)
    fxy = X**2 + Y**2
    plt.contour(X,Y,fxy, levels = [R**2])
    fxy = (X**2/a**2)+(Y**2/b**2)
    plt.contour(X,Y,fxy, levels = [1])
    plt.plot(x,y,color ='b', label = 'my_circl')
    plt.title('plotter')
    plt.legend()
    plt.show()
ell_circl_plotter()