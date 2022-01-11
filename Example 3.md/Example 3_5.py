# -*- coding: utf-8 -*-
# Example3_5.py
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([-0.090,-0.039,0,0.036,0.092,0.136,0.183])
y1 = np.array([0.2810,0.5965,0.7184,0.6138,0.2939,0.0778,0.0259])
plt.plot(x1,y1,'s')

def my_Gaussian(x):
    return M*np.exp(-x*x/(4*D*t))/(np.sqrt(4*np.pi*D*t))

t = 6000
D = 1e-6
M = 0.1

X = np.linspace(-0.35,0.35,500)
Y = my_Gaussian(X)
plt.plot([],[],'',label='D values')
plt.plot(X,Y,label=D)

while D!= 0:
#    plt.pause(0.1)
    x = input('D={:.8}; enter value for D (or zero to exit): '.format(D))
    D = float(x)
    if D==0: break

    x = input('M={:.8}; enter value for M (or zero to exit): '.format(M))
    M = float(x)
    if M==0: break

    Y = my_Gaussian(X)
    plt.plot(X,Y,label=D)

plt.show()
