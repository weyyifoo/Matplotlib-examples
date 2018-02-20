# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:57:41 2018

@author: Wey Yi
"""

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)

t1 = np.arange(0, 3, 0.1)

plt.figure(1)

plt.subplot(411)
plt.grid(True)
plt.axis([0, 3, -3, 3])
plt.plot(t1, f(t1), 'bo', t1, f(t1), 'k')

plt.subplot(412)
plt.grid(True)
plt.axis([0, 3, -3, 3])
plt.plot(t1, 2 * f(t1), 'bo', t1, 2 * f(t1), 'k')

plt.subplot(413)
plt.grid(True)
plt.axis([0, 3, -3, 3])
plt.plot(t1, np.cos(2 * np.pi * t1), 'bo', t1, np.cos(2 * np.pi * t1), 'k')

plt.subplot(414)
plt.grid(True)
plt.axis([0, 3, -3, 3])
plt.plot(t1, 2 * f(t1) + np.cos(2 * np.pi * t1), 'bo', t1, 2 * f(t1) + np.cos(2 * np.pi * t1), 'k')

plt.show()