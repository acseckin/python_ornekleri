# -*- coding: utf-8 -*-
"""
@author: acs
"""
import numpy as np
from matplotlib import pyplot

def kosinusCiz(gelenDeger):
    y=np.cos(2*np.pi*1.0*gelenDeger)*1.5
    pyplot.plot(gelenDeger,y)
    pyplot.ylim(-2, 2)
    pyplot.xlim(0, 1.0)
def sinusCiz(gelenDeger):
    y=np.sin(2*np.pi*1.0*gelenDeger)*1
    pyplot.plot(gelenDeger,y)
    pyplot.ylim(-2, 2)
    pyplot.xlim(0, 1.0)

x=np.linspace(0,1,100)
pyplot.subplot(1,2,1)
kosinusCiz(x)
pyplot.grid()
pyplot.subplot(1,2,2)
sinusCiz(x)
pyplot.grid()
