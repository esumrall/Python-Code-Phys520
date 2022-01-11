# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:17:44 2022

@author: beardda
"""
# Example3_5b.py
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([-0.090,-0.039,0,0.036,0.092,0.136,0.183])
y1 = np.array([0.2810,0.5965,0.7184,0.6138,0.2939,0.0778,0.0259])
plt.plot(x1,y1,'s')

def my_Gaussian(x):
    return M*np.exp(-x*x/(4*D*t))/(np.sqrt(4*np.pi*D*t))

t = 6000
D = 0.39e-6
M = 0.12

X = np.linspace(-0.35,0.35,500)
Y = my_Gaussian(X)
plt.plot([],[],'',label='D values')
plt.plot(X,Y,label=D)


plt.show()
