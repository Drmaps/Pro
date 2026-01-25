import random
uzunluk = int(input("şifrenizin uzunluğunu belirleryiniz:"))
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre = ''
for i in range(uzunluk) :
    sifre = sifre + random.choice(karakter)
print(sifre)
