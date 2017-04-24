#Soru 3
from sympy.solvers import solve
from sympy import Symbol
import numpy as np
from matplotlib import pyplot as plt

x = Symbol('x')
y = np.arange(-2,2,0.1)
xp=[]
for yi in y:
    sol=solve((x**3)+2*(x**2)*yi+7*x*(yi**2)+8,x)
    print sol
    xp.append(sol[0])
plt.plot(y,xp)
plt.grid()
