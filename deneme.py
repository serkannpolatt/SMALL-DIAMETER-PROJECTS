# BÜYÜK OLAN SAYIYI BULMA

# x=int(input("lütfen 1. değeri giriniz : "))
# y=int(input("lütfen 2. değeri giriniz :"))

# if x>y or y<x:
    # print("büyük olan sayı x değeridir")
# elif y>x or x<y:
    # print("büyük olan y değeridir ")
# else:
    # print("iki sayı birbirine eşittir")    

# SAYIYI 5'ER AZALT VE YAZDIR

# sayi=int(input("lütfen azaltıcağınız değeri giriniz :"))

# while sayi > 0:
    # sayi-=5
    # print(sayi)


# LİSTEDEKİ SAYILARIN ORTALAMASI

# liste=[50,90,30,60]
# liste2=[69,97,31,50]
# def ortalamahesapla(x):
    # sayac=0
    # for i in x:
        # sayac=i+sayac
        # uzunluk=len(x)
        # ortalama=sayac/uzunluk
    # print(ortalama)
    
# ortalamahesapla(liste2)


#  İSİM SORUP LİSTEYE EKLEME

# namelist=[]

# kac=int(input("lütfen istedğiniz isim kadar sayı girinizi: "))

# while len(namelist) < kac:
    # isim=input("lütfen isim giriniz : ")
    # namelist.append((isim))

# print(namelist)


# ÇARPI İFADELİ ÇARPIM TABLOSU

# x=1

# while x<=9:
    # y=1

    # while y<=9:
        # print(x,y,x*y* '*')
        # y+=1
        # x+=1


# BİR SAYIYA TAM BÖLÜNEN VE BİR SAYININ KATI OLMAYAN

# listem=[ ]

# x=int(input("1. değeri giriniz :"))
# y=int(input("2. değeri giriniz :"))

# for i in range(x,y):

    # if i%7 == 0 and i%3 != 0:
    #    listem.append(str(i))

# print(','.join(listem))




