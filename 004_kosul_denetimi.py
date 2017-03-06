#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:25:56 2017

@author: acseckin
"""
import time

ilkzaman=time.time()

sayi=0

if sayi>10:
    print "Sayı 10'dan büyük"
    time.sleep(1)
if sayi<10:
    print "Sayı 10'dan küçük"  
    time.sleep(1)
if (sayi%2)>0:
    print "Sayı ikiye tam bölünmez"
    time.sleep(1)
if (sayi%2)==0:
    print "Sayı ikiye tam bölünür"
    time.sleep(1)
    
sonzaman=time.time()

gecensure=sonzaman-ilkzaman
print gecensure