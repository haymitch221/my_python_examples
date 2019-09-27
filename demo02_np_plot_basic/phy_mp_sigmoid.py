import numpy as np
import matplotlib.pyplot as mp

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))


x = np.arange(0, 50, 1)
# 用切片实现映射
y1 = np.array([np.exp( - xi ) for xi in x])
y2 = np.array([nonlin(xi) for xi in x])

mp.plot(x, y1)
mp.plot(x, y2)
mp.show()