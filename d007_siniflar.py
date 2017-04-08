class Ogrenci:
   OS = 0 # sınıf değişkeni, tüm örneklerde bu değer paylaşılır
   def __init__(self, name, number): # özel bir metottur, sınıf yapılandırıcısı, ilk çalıştırmada etkindir.
      self.ad = name
      self.numara = number
      Ogrenci.OS += 1
   def ogrenciSayisiYaz(self):
     print "Toplam Ogrenci Sayisi %d" % Ogrenci.OS
   def OgrenciBilgiYaz(self):
      print "Ad: ", self.ad, ", Ogrenci No: ", self.numara

ogr1 = Ogrenci("Ahmet", 123)
ogr1.OgrenciBilgiYaz()
ogr1.ogrenciSayisiYaz()
ogr2 = Ogrenci("Ayse", 555)
ogr2.OgrenciBilgiYaz()
ogr2.ogrenciSayisiYaz()
ogr3 = Ogrenci("Fatih", 007)
ogr3.OgrenciBilgiYaz()
ogr3.ogrenciSayisiYaz()
