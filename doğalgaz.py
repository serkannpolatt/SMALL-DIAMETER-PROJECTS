Ocak=31
Şubat=28
Mart=31
Nisan=30
Mayıs=31
Haziran=30
Temmuz=31
Ağustos=31
Eylül=30
Ekim=31
Kasım=30
Aralık=31

a=input("Hangi aydaki doğalgaz harcamanızı hesaplamak istersiniz? Lütfen ay adını hepsinin baş harfini büyük olarak yazınız : ")
hangiAy=eval(a)

birimFiyat=1.68

b=input("Günlük doğalgaz harcama belirtiniz: ")
günlükharcama=eval(b)

aylikharcama=hangiAy*birimFiyat*günlükharcama

print(aylikharcama)