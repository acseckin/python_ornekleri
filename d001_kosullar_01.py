#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Koşul denetimi
"""

print "Program Baslangıcı"
sayi=0

while (sayi<=10):
    sayi=input("Bir sayı giriniz:")
print "Sayı 10'dan büyük"

while (True):
    sayi=input("Bir sayı giriniz:")
    if sayi>10:
        break
print "Sayı 10'dan büyük"
