                                     #          DEĞİŞKENLER             #
 



# sayi = 35
# print(sayi)
# sayi = 55
# print(sayi)

# ondalikli_sayi = 56.7
# print(ondalikli_sayi)

# islem = 10 / 3
# print(islem)




                                      #          OPERETÖRLER        #




sayi1 = 35
sayi2 = 65

print(sayi1 + sayi2)
print(sayi1 - sayi2)
print(sayi1 * sayi2)
print(sayi1 / sayi2)


# print(sayi1 > sayi2)
# print(sayi1 < sayi2)

# sayi1 += 1
# print(sayi1)

# sayi2 -= 1
# print(sayi2)






                                      #          STRİNGSLER            #



# isim = "Bahadır"
# print(isim)

# name = "Mustafa"
# surname = "Doğrusöz"

# print(name + " " + surname)

# metin = "Hello Türkiye"
# print(metin[2:7])

# print(metin.lower())
# print(metin.upper())       





                                        #          CASTİNGSLER           #




# sayi = int(input("Bir sayı giriniz: "))
# print(sayi)
# print(type(sayi))                        



                      


                                        #           LİSTELER              #



# liste = ["Osman",15,False]
# print(liste[0])

# liste.append("Ayşe")
# print(liste)

# liste2 = ["Konya","Adana","İzmir"]
# liste.extend(liste2)
# print(liste) 



                      

                                       #          DEMETLER (TUPLES)        #




# demet = ("Ankara","Sinop","Hatay")
# print(type(demet))
# print(demet)
# demet[0] = "İstanbul"
# print(demet)





                                       #           DİCTİONARY             #




# iller = {"Kayseri":"Mantı","Adana":"Kebap","İzmir":"Boyoz"}
# print(iller)
# print(iller["Kayseri"])
   


                     
                        
                                            #        IF-ELSE-OR-AND          #



# number = 30

# if number > 10:
#     print("Sayı 10'dan büyük")

# else:
#     print("Sayı 10 veya 10'dan küçüktür")

# print("-------------------------------------------------")

# weather = "Güneşli"

# if weather == "Yağmurlu":
#     print("Hava yağmurlu")

# elif weather == "Güneşli":
#     print("Hava güneşlidir")

# elif weather == "Karlı":
#     print("Hava karlıdır")

# else:
#     print("Hava bulutludur")

# print("-------------------------------------------------")

# username = input("Kullanıcı adınızı giriniz: ")
# password = input("Şifrenizi giriniz: ")

# if username == "boncuk" and password == "12345678":
#     print("Sisteme başarıyla giriş yaptınız! Tebrikler")

# else:
#     print("Kullanıcı adı veya şifre yanlış")

# print("-------------------------------------------------")

# number2 = int(input("Bir sayı giriniz: "))

# if number2 % 2 == 0 or number2 % 3 == 0:
#     print("Sayı ikiye ve üçe veya ikisinden birisine bölünebiliyor!")

# else:
#     print("Sayı ne ikiye ne de üçe bölünemiyor!")


                       



                                  #         DÖNGÜLER=FOR-BRAK-WHİLE-COUNTİNE          #




# liste = ["Adana","Ankara","İzmir","Kayseri"]

# for sehirler in liste:
#     print(sehirler)


# print("--------------------------------------------")

# maaslar = [1500,1750,3500,5400]

# for maas in maaslar:
#     if maas > 1000 and maas < 2000:
#         yeni_maas = maas + 200
#         print(yeni_maas)

# print("--------------------------------------------")

# sayilar = [1,2,3,4]

# for sayi in sayilar:
#     print(sayi)
#     if sayi == 2:
#         break
# print("--------------------------------------------")

# for sayi1 in sayilar:
#     print(sayi1)
#     if sayi == 2:
#         continue

# print("--------------------------------------------")
# print("While Kullanımı")

# i = 1
# while i < 6:
#     print(i)
#     i += 1







                                           #             FONKSİYONLAR           #

# def ekrana_yazdir():
#     print("Ben bir fonksiyonum")

# ekrana_yazdir()

# print("----------------------------------------------------")

# def karesini_al(x):
#     print(x * x)

# number = int(input("Karesi alınacak sayıyı giriniz: "))
# karesini_al(number)

# print("----------------------------------------------------")

# def toplama(z,t):
#     return z + t

# print(toplama(10,20))

# print("----------------------------------------------------")

# us_al = lambda a,b:a**b

# print(us_al(2,4))








                                        #                  KALITIM               #

# class Araba:
#     marka = ""
#     cikis_yili = 0
#     km = 0
#     lpg = True
#
# araba1 = Araba()
# araba1.marka = "Renault"
# araba1.cikis_yili = 2009
# araba1.km = 32000
# araba1.lpg = False
#
# print(araba1.marka)
# print(araba1.cikis_yili)
# print(araba1.km)
# print(araba1.lpg)

# class Muzisyen:
#     def __init__(self,isim,tur):
#         self.isim = isim
#         self.tur = tur
#
# muzisyen1 = Muzisyen("Beethoven","Klasik")
# muzisyen2 = Muzisyen("Ajdar","Pop")
# muzisyen3 = Muzisyen("Ceza","Rap")
# muzisyen4 = Muzisyen("Lars","Rock")
#
# print(muzisyen1.isim)
# print(muzisyen1.tur)
# print("----------------------------------")
# print(muzisyen2.isim)
# print(muzisyen2.tur)
# print("----------------------------------")
# print(muzisyen3.isim)
# print(muzisyen3.tur)
# print("----------------------------------")
# print(muzisyen4.isim)
# print(muzisyen4.tur)


# class Sinif1:
#     def yazdir(self):
#         print("Yazdırıldı")

# class Sinif2(Sinif1):
#     def yazdir_iki(self):
#         print("Yazdıracak mısın?")

# sinif2 = Sinif2()
# sinif2.yazdir_iki()
# sinif2.yazdir()







                               #                HATA     YÖNETİMİ               #

# try:
#     number = int(input("Bir sayı giriniz: "))
#     print(number)

# except ValueError:
#     print("Lütfen bir sayı giriniz metin girmeyiniz")
#     number = int(input("Bir sayı giriniz: "))
#     print(number)




                            