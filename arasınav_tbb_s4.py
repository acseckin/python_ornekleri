# Soru 4
element = ""
tur = -1
cikti = ""
def turOgren(deger):#okunan karakterlerin büyük,küçük veya sayı olup olmadığını bu fonksiyon saysinde anlıyoruz.
    if ord(deger) >= 65 and ord(deger) < 91:#karakterin ascii kodu bu değer aralığındaysa büyük harf
        return 2
    elif ord(deger) >= 97 and ord(deger) < 123:#karakterin ascii kodu bu değer aralığındaysa küçük harf
        return 1
    elif ord(deger) >= 49 and ord(deger) < 58:#karakterin ascii kodu bu değer aralığındaysa sayı
        return 0
def elementAyristir(element):#bileşikten ayırdığımız her elementi bu fonksiyonda ayrıştırıyoruz.
    transElement = ""
    adet = ""
    for j in element:
        tur = turOgren(j)
        if tur == 2 or tur == 1:
            transElement = transElement + j
        elif tur == 0:
            adet = adet + j
    if adet == "":#eğer elementten 1 tane varsa bunu if şartı ile kontrol ediyoruz.
        adet = "1"
    print transElement,"elementinden",adet,"tane var" 
while (True):
    giris=raw_input("element giriniz: ")
    for i in giris:
        tur = turOgren(i)
        if tur == 2:#buyuk harf
            if element == "":
                element = i
            else:
                elementAyristir(element)
                element = i
        elif tur == 1 :#kucuk harf
            element = element + i    
        elif tur == 0:#sayi
            element = element + i
    elementAyristir(element)
    element = ""
    tur = -1
