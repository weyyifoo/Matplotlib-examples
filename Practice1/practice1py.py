# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:54:25 2018

@author: Wey Yi
"""

import matplotlib.pyplot as plt
import numpy as np

n = np.arange(0, 100, 0.5)

plt.figure(1)

def f(n):
    y = np.exp(n)
    return y

plt.subplot(311)
plt.plot(n, f(n), '-bo')

plt.show()