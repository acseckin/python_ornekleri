import numpy as np
import matplotlib.pyplot as plt


t1 = np.arange(0.0, 5.0, 0.1)
f1= np.exp(-t1) * np.cos(2*np.pi*t1)

t2 = np.arange(0.0, 5.0, 0.02)
f2= np.exp(-t2) * np.cos(2*np.pi*t2)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f1, 'bo', t2, f2, 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
