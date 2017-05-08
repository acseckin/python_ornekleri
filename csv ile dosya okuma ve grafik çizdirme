# -*- coding: utf-8 -*-
"""
Created on Mon May 08 14:04:28 2017

@author: Pc
"""

import csv
import matplotlib.pyplot as plt
   
xdeg=[0]
xtur=[0]
xint=[0]

ydeg=[0]
zdeg=[0]   
zaman=0.1    
try:      
    csvval = csv.reader(open("deneme.csv", "rb"))
    csvval_list = []
    csvval_list.extend(csvval)
    i=0
    for data in csvval_list: 
        #print float(data[0]), float(data[1]), float(data[2])
        xdeg.append(float(data[0]))
        xtur.append((xdeg[-1]-xdeg[i])/zaman)
        i=i+1
        xint.append((xint[-1]+xdeg[-1])*zaman)
        ydeg.append(float(data[1]))
        zdeg.append(int(data[2]))
    print xdeg
except:
    print "dosya hatası"

plt.subplot(2,2,1)
plt.plot(xdeg,'r')
plt.plot(ydeg,'b')
plt.plot(zdeg,'g')

plt.subplot(2,2,2)
plt.plot(xdeg,'g')
plt.plot(xtur,'r')
plt.plot(xint,'b')

plt.subplot(2,1,2)
plt.plot(xdeg,ydeg,'r')
