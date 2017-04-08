#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:47:42 2017

@author: acseckin
"""

import random

rastgele=random.randint(0,10)
while (True):
    giris=input("Deger giriniz:")
    if giris<rastgele:
        print "degeriniz kucuk"
    elif giris>rastgele:
        print "deger buyuk"
    else:
        print "Buldunuz"
        break
