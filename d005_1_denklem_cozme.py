#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 16:15:23 2017

@author: acs
"""

from sympy.solvers import solve
#sympy komutuyla solvers komutunu çalıştırıyoruz.
from sympy import Symbol
import numpy as np
from matplotlib import pyplot as plt
#import yaparak matematiksel işlemleri yapıyoruz.
#koordinat düzlemimde x ve y'yi tanımlıyoruz
x = Symbol('x')
#symbol komutunu x'e tanımlıyoruz.
y = np.arange(-1.0,1.01,0.1)
#arange komutuyla koordinatları giriyoruz
xp=[]
xn=[]
#for döngüsünü kullanarak dairenin matematiksel komutlarını giriyoruz
for yi in y:
    sol=solve(x**2 +yi**2-1.0,x)
    print sol
    xp.append(sol[0])
    xn.append(sol[-1])
    print xp[-1],xn[-1]
plt.plot(xp,y)
plt.plot(xn,y)


