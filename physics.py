import math

#Yer cekimi
g= 9.8

#Degiskenlerin alinmasi
print("-----------------------------------------------------------------")
yukseklik = int(input("Yuksekligi giriniz: "))
baslangic_hizi = int(input("Varsa baslangic hizi: "))
print("-----------------------------------------------------------------")

#Degiskenlerin gerekli degerlere atanmasi
h= yukseklik
vy= baslangic_hizi

# t degerini hesaplamak icin diskriminant a cevirilmis formul
#1/2g = a, vy = b, h = c
# at^2+bt+c=0
# t = -vy + kare kok(vy^2 + 4.g.h)/2.g
sqrt_part = math.sqrt(vy**2 + 2*g*h)

#Sure hesaplama formulu
sure = (-vy + sqrt_part) /g
t = sure

#Hiz hesaplama
v= g*t
print()
print("-----------------------------------------------------------------")
print("Yere dusus suresi: ",t," saniye")
print("dustugu zaman hizi: ",v," m/s")
print("-----------------------------------------------------------------")
print()
print()
#Uptade time
print("-----------------------------------------------------------------")
print("Mevcut yere dusus suresinden daha kucuk bir sayi giriniz: ", int(sure))
t = int(input("istediginiz sureyi giriniz: "))
print("-----------------------------------------------------------------")

#Uptate height
h= 0.5*g*t**2
#Update velocity
v= g*t
kalan_h = yukseklik - h
print()
print()
print("-----------------------------------------------------------------")
print("Guncellenen zaman katsayisina gore yeni alinan yol: ",h," metre")
print("Çarpmaya kalan yol: ", kalan_h," metre")
print("Yeni yukseklikteki Anlik hiz: ",v," m/s")
print("-----------------------------------------------------------------")
print()
print()