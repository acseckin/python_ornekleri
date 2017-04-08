import numpy as np

# matris oluşturma
a=np.array([[1,2],[3,4]])
b=np.array([[11,12],[13,14]])

# boyut öğrenme
aninboyutu=a.shape

# transpoz
bnintranspozu=b.T

# nokta çarpım
nc=np.dot(a,b)
"""
|1∗11+2∗13  1∗12+2∗14|    |37 40|
|3∗11+4∗13  3∗12+4∗14| =  |85 92|
"""

# iç çarpım
ic=np.inner(a,b)
"""
|1∗11+2∗12  1∗13+2∗14|    |35 41|
|3∗11+4∗12  3∗13+4∗14| =  |81 95|
"""

# vektör ve matris çarpımı
v=np.matrix("4.;5.")
m=np.matrix([[1.,2], [3,4], [5,6]])
s1=A*x

# matrisin rankı
A=np.array([[11,12],[13,14],[15,16],[20,20]])
rank=np.linalg.matrix_rank(A)

#denklem çözme Ax=b şeklindeki denklemi çözme
A = np.array([[1,2],[3,4]])
b = np.array([10, 20])
x = numpy.linalg.solve(A,b)

#özdeğer bulma
ozdegerA=numpy.linalg.eig(A)
