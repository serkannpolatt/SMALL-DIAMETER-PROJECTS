# 1- Kullanıcıdan ismini alarak "Merhaba isim" yazan programı yazınız?


# isim = input("merhaba isminiz?: ")
# print("merhaba",isim)






# 2- Kullanıcıdan iki sayı alarak bunların toplamını ve ortalamasını ekrana yazan programı yazınız?





# s1=int(input("birinci sayı? ="))
# s2=int(input("ikinci sayı ? = "))

# toplam=s1+s2
# ortalama= toplam/2
# print("toplam =",toplam)
# print("ortalama =",ortalama)





# 3- Kullanıcıdan alınan 3 sayının en büyüğünü bulan programı yazınız?





# x= int(input("sayı giriniz: "))
# y= int(input("sayı giriniz: "))
# z= int(input("sayı giriniz: "))
# numers = []
# numers.append(x)
# numers.append(y)
# numers.append(z)
# numers.sort()
# print("En büyük sayı : ",numers[-1])






# 4- Vize notunun %40'ını, Final notunun %60'ını alarak ortalama notu hesaplayan, ortalama 50 den büyükse "Geçti", küçükse "Kaldı" yazan programı yazınız?
v = int(input("vize:"))
f = int(input("final"))
ortalama = v*0.40+f*0.60
print("ortalama =",ortalama)
if ortalama>=50:

      print("geçti")
else:
       print("kaldı")





# 5- 1'den 100'e kadar olan sayıların toplamını bulunuz?




# toplam=0
# for i in range(100):
#     toplam +=i
# print ("1 den 100e kadar olan sayıların toplamı",toplam)





# 6- 1'den n'e kadar olan sayılardan tek olanların toplamını bulunuz? n sayısı kullanıcıdan alınacaktır



# n = int(input("n sayısı: "))
# toplam = 0
# for i in range (n):
#      if i%2==1:
#          toplam +=i
# print("tek sayıların toplamı",toplam)





# 7- n'den m'ye kadar olan sayılardan 7'ye tam bölünenleri bulunuz? n başlangıç ve m bitiş sayısı kullanıcıdan alınacaktır. 



# while True:

#     n=int(input("başlangıçtakı sayı girin:"))
#     m=int(input("sondaki sayı girin:"))
#     if n>=m:
#          print("başlangıçtaki daha küçük olmalı")
#     else:
#      break
# toplam=0
# for i in range(n,m):
#     if i%7==0:
#         toplam += i
#         print("yediye tam bölünenelerin toplamı=", toplam)





# 8- Kullanıcıdan ismini alıp ekrana tersten yazan programı yazınız?



# isim=input("isminizi girin:")
# isim= isim[::-1]
# print(isim)




# 9- 0 ile 1000 arasındaki Fibonacci sayılarını bulan programı yazınız?

# a=1
# b=1
# c=0
# while c<1000:
#     print(b)
#     c=a+b
#     a=b
#     b=c





# 10- 0 ile 1000 arasındaki Asal sayıları bulan programı yazınız?





# for sayı in range(1,1000):
#     if sayı>1:
#         for i in  range (2,sayı):
#          if(sayı % i)==0:
#              break
#         else:
#                 print(sayı)





# 11- Kullanıcının istediği kadar sayıyı, kullanıcıdan alarak bir diziye aktaran, bu sayıların toplamını ve ortalamasını bulan programını yazınız?





# adet=int(input("kaç adet sayı girmek?"))

# dizi = []

# for i in range(adet):

#     dizi.append(int(input("sayı giriniz:")))

# print(dizi)

# toplam=0
# for x in dizi:
#     toplam+=x
# print("toplam",toplam)
# print("ortalama", toplam/adet)







# 12-Maaşlara zam yapma

# maaslar=[2000,3000,2999,1231,9780,19000]

# for maas in maaslar:

#  if maas>=2000 and maas<4000:

#      yeni_maas= maas+600

# print(yeni_maas)




# 13- 0-100 arasında girilen puan değerine göre not değeri hesaplama

# puan=int(input("puan değerini giriniz:"))

# if puan  < 0 or puan > 100:
#      print("lütfen 0-100 aralığında değer giriniz")

# else:

#     if puan >=90:
#         harf_notu="AA"
#     elif puan >=80:
#          harf_notu="BA"
#     elif puan >=70:
#          harf_notu="BB"
#     elif puan >=60:
#          harf_notu="CB"
#     elif puan >=50:
#          harf_notu="CC"
#     elif puan >=40:
#          harf_notu="DC"
#     else: 
#          harf_notu="FF"
#     print(f"{harf_notu}") 

# 14- delta

# import math
# a=int(input("a değerini giriniz:"))
# b=int(input("b değerini giriniz:"))
# c=int(input("c değerini giriniz"))

# delta=b*b-4*a*c
# if delta <0:
#     print("denkleminin reel kökü yoktur")
# elif delta ==0:
#     kok=(-b)/(2*a)
#     print(f"denkleminin tek kökü var:{kok}")
# else:
#     kok1=(-b+math.sqrt(delta))/(2*a)
#     kok2=(-b-math.sqrt(delta))/(2*a)
#     print(f"denkleminin iki kökü var: {kok1},{kok2}")

# 15- Kullanıcı adı şifre

# kullanici_adı=input("kullanıcı adınızı giriniz:")
# sifre=input("şifrenizi giriniz:")
# if kullanici_adı == "serkan" and sifre=="3131":
    #  print("hoşgeldiniz")
# else:
    #  print("kullanıcı adı veya şifre hatalı.Lütfen tekrar deneyiniz")    




# 16-sayı tahmin            

# import random      

# sayi =random.randint(1,100)
# can =int(input("kaç hak istersiniz:"))
# hak=5
# sayac = 0

# while hak >0:
    #  hak=-1
    #  tahmin =int(input("tahmin :"))
    #  if sayi == tahmin:
        #  print(f"tebrikler {sayac}. defada bildiniz. Toplam puanınız:{100-(100/can) * (sayac-1)}")
        #  break
    #  elif sayi >tahmin:
        #  print("yukarı")
    #  else:
        #  print("aşağı")
    #  if hak == 0:
        #  print(f"hakkınız bitti: {sayi}")


