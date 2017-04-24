#Soru 2
def asalbul(baslangic, bitis):
    asalsayilar=[]
    asaldegil=0
    for s in range(baslangic,bitis):
        print s,
        if s<2:
            asaldegil=1
            print "asal degil"
        elif s>=2:
            for b in range(2,s):
                if s%b==0:
                    print "asal degil"
                    asaldegil=1
                    break
        if asaldegil==0:
            print "asal"
            asalsayilar.append(s)
        asaldegil=0
    return asalsayilar

print asalbul(-5,20)
