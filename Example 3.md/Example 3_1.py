# -*- coding: utf-8 -*-
# First example: Example3_1.py
import numpy as np
import matplotlib.pyplot as plt

def my_Gaussian(x):
    return A*np.exp(-x*x/B)

A,B = 1,1
X=np.linspace(-4,4,200)
Y=my_Gaussian(X)

plt.plot(X,Y,'k')

# dX = X[2]-X[1]
# area = dX*sum(Y)
# print(area)