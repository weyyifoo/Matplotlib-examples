# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:59:28 2018

@author: Wey Yi
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def f1(n):
    y = np.sin(n)
    return y

x = np.arange(0, 100, 0.1)
y = f1(x)

fig1 = plt.figure(1)
plt.subplot(311)
plt.plot(x, y, 'bo')

fig2 = plt.figure(2)
plt.subplot(211)
plt.plot(y,x,'rd')
plt.show()