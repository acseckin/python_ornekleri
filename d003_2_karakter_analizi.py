# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:40:59 2017

@author: acseckin
"""

girisdeger="19"

Asayisi=0
asayisi=0
for g in girisdeger:
    print ord(g)
    if ord(g)>=65 and ord(g)<97:
        print "Buyuk Harf:",g
    if ord(g)>=49 and ord(g)<58:
        print "Sayı:", int(g)
    
    """
    if 'A' ==g:
        print "Yazi icinde A harfi var"
        Asayisi=Asayisi+1
    if 'a' ==g:
        print "Yazi icinde a harfi var"
        asayisi=asayisi+1
    """
        
