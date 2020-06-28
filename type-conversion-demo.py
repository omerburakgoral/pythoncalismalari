'''
Daire Alanı: pir2
Daire Çevresi: 2pir

* Yarı çapı verilen bir dairenin alanı ve çevresini
hesaplayınız.   (r: 3,14)
'''
pi = 3.14

r = float(input("yarıçap:   "))
alan = pi * (r ** 2)
cevre = 2 * pi * r
print(" alan: " + str(alan) + " çevre: " + str(cevre))
input('Press ENTER to exit')
