# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 15:59:28 2018

@author: Wey Yi
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def f1(n1):
    y1 = np.sin(n1)
    return y1

def f2(n2):
    y2 = np.exp(n2)
    return y2

x1 = np.arange(0, 100, 0.1)
y1 = f1(x1)
x2 = np.arange(0, 5, 0.1)
y2 = f2(x2)

fig1 = plt.figure(1)
plt.subplot(211)
plt.plot(x1, y1, 'bo')
plt.subplot(212)
plt.plot(y1,x1,'rd')

fig2 = plt.figure(2)
plt.subplot(211)
plt.plot(x2, y2, 'rs')
plt.subplot(212)
plt.plot(y2, x2, 'k-')

plt.show()