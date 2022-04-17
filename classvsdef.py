
#fsayi=int(input("ilk sayı gir "))
#ssayi=int(input("ikinci sayı gir "))


#isim=input("isim gir: ")
#soyisim=input("soyisim giriniz : ")
#yas=int(input("lütfen yası giriniz : "))
class Matematik:
    def __init__(self,a,b):
        self.ilksayi=a
        self.ikincisayi=b

    def topla(self):
        return self.ilksayi+self.ikincisayi

    def carpma(self):
        return self.ilksayi*self.ikincisayi


    def bolme(self):
        return self.ilksayi/self.ikincisayi

    def cikarma(self):
        return self.ilksayi-self.ikincisayi





#matemaik=Matematik(fsayi,ssayi)




def isimyaz(name):
    print(name)


isimyaz("mert")



#print(matemaik.topla())
#print(matemaik.cikarma())




class person:
    def __init__(self,name,surname,age):
        self.name=name
        self.surname = surname
        self.age=age


#defaultperson=person(isim,soyisim,yas)
#print(defaultperson.name)
#print(defaultperson.surname)
#print(defaultperson.age)




isimyaz("hamza")