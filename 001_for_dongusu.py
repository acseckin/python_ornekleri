#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
For Döngüsü

cok satirli
aciklama
Uşak Universitesi
"""
# tek satır aciklama

import numpy 
print "Program Baslangıcı"
print "0-10 arası 1.7 artarak"
elemanlar=numpy.arange(0,10,1.7)
print "Sayı\t(3)\t(5)\t(7)"
for e in elemanlar:
    print e,"\t", e%3,"\t", e%5,"\t", e%7
print "Herhangi bir liste"
elemanlar=[3,8,7.2,85]
print "Sayı\t(3)\t(5)\t(7)"
for e in elemanlar:
    print e,"\t", e%3,"\t", e%5,"\t", e%7
print "Program Sonu"