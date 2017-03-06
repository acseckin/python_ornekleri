#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:00:29 2017

@author: acseckin
"""

ad="uşak üniv"
siralanmis=[]

i=0
while (True):
   print ad[i],"<",ad[i+1], ad[i]<ad[i+1]
   if (ad[i]<ad[i+1])==False:
       siralanmis.append(ad[i+1])
   else:
       siralanmis.append(ad[i])
   i=i+1
   if i+1==len(ad):
       break

print siralanmis