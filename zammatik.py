yeniMaas=0
maas=input("Maaşı Gir : ")
zam=input("Zam Oranı(%) : ")
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamlı Maaş :",yeniMaas)



serkanhesap= {
 'ad':'Serkan Polat',
 'hesapNo':'315261',
 'bakiye':4300,
 'ekHesap':6000,
 'maas':3290
  }


sekohesap= {
 'ad':'seko',
 'hesapNo':'333331',
 'bakiye':3333,
 'ekHesap':6033,
  "maas":4342}
 

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap["bakiye"]>=miktar):
       hesap["bakiye"]-=miktar
       print("paranızı alabilirsiniz")
       bakiyesorgulama(hesap)

    else:
        toplam= hesap['bakiye'] + hesap['ekHesap']

        if (toplam>=miktar):
           ekhasapkullanimi=input('ek hesap kullanılsın mı (y/n)')
           
           if ekhasapkullanimi=='y':
              ekhasapkullanilacakmiktar=miktar-hesap['bakiye']
              hesap["bakiye"]=0
              hesap["ekHesap"]-=ekhasapkullanilacakmiktar
              print('paranızı alabilirsniz')
              bakiyesorgulama(hesap)

           else:
              print(f"{hesap['hesapno']} nolu hesabınıza {hesap['bakiye']} bulunuyor.")      
        else:
           print("bakiyeniz yetersiz")
           bakiyesorgulama(hesap)

def bakiyesorgulama(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunuyor.Ek hesabınızda limitiniz ise {hesap['ekHesap']} tl bulunuyor")

paraCek(serkanhesap, 1999)
 
 