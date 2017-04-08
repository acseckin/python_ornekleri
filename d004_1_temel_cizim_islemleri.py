#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:52:20 2017

@author: acs
"""

import numpy as np
from matplotlib import pyplot as plt

# cosinus cizimi
x=np.arange(0,100,0.1)
y=np.cos(x)

plt.plot(x,y)
plt.show()

# cosinus ciziminin limitlerinin ayarlanması
"""
plt.ylim(-2, 2)
plt.xlim(0, 10.0)
"""
