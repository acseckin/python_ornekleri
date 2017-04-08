#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:00:29 2017

@author: acseckin
"""

ad="programlamadersi"
for a in ad:
    print a ,ord(a)
i=0
while (True):
   print i, ad[i], ad[i+1],"\t"
   if (ad[i]>ad[i+1]):
       print ad[i:i+1],">>",ad[i+1:i:-1],
       ad=ad[0:i]+ad[i+1]+ad[i]+ad[i+2:]
       print ad
       i=0
   else:
       i=i+1
   if i+1==len(ad):
       break

print "Son Hal:",ad
