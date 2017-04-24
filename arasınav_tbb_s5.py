#Soru 5 a 
import numpy as np
ad="AhmetCagdasSeckin01045450"
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
print "Kucukten Buyuge:",ad
bk=""
for i in np.arange(len(ad)-1,-1,-1):
    bk=bk+ad[i]
print "Buyukten kucuge",bk

# Soru 5 b
sayiadet=0
buyukadet=0
kucukadet=0
for s in ad:
    ord(s)
    if ord(s)>=97:
        kucukadet=kucukadet+1
    elif ord(s)>=65:
        buyukadet=buyukadet+1
    elif ord(s)>=48:
        sayiadet=sayiadet+1
print "Kucuk harf adet:",kucukadet
print "Buyuk harf adet:",buyukadet
print "Sayi adet:",sayiadet
