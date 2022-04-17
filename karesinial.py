



sayi=int(input("lütfen sayı aralığını giriniz : "))

mydict={}

def karealekle(x):

    for i in range(1,sayi+1):
        mydict[i]=i**2
    print(mydict)

karealekle(sayi)

print("sonuc : ",mydict[4])