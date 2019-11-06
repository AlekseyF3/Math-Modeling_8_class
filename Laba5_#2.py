import matplotlib.pyplot as plt
import numpy as np
def par_gip_plotter(a = 1,b = 1,c = 0,k = 2, title = 'par.plotter'):
    x = np.arange(-10,-0.1,0.01)
    y = a*x**2 + b**2 + c
    y = k/x
    plt.plot(x,y,color ='b', label = 'my_par')
    plt.title('plotter')
    plt.legend()
    plt.show()
par_gip_plotter()
    
    