# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:41:59 2018

@author: Wey Yi
"""

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled data at 500ms intervals

t = np.arange(0, 10, 0.5)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.axes([0, 10, 0, 5000])
plt.show()