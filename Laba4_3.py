from const4 import g

def fly(m, V, h):
    E=((m*V**2)/2)+((m*g*h)/2)
    print(E)


fly(10, 20, 200)

