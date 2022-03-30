



#kendisi ve 1 dışında başka hiçbir sayıya tam olarak bölünemeyen sayılara asal sayı denir.

#bir asal sayı 1'den büyük olmalı

sayi=int(input("lütfen bir sayı giriniz : "))

if sayi > 1 :

    for x in range(2,sayi):
        if (sayi % x) == 0:
            print("asal değildir")
            break

    else:
        print("sayı asaldır")
else:
    print("Sayı asal değildir çünkü 1'den küçük bir sayı girdiniz")


