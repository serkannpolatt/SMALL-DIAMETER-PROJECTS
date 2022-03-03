



liste=[1,4,6,7,5,8]

liste2=[50,40,10,20]

def ortalamahesapla(x):
    sayac=0
    for i in x:
        sayac=i+sayac
        uzunluk=len(x)
        ortalama=sayac/uzunluk
    print(int(ortalama))



ortalamahesapla(liste2)