"""
Musteri adi
Musteri soyadi
musteri ad+soyad
musteri cinsiyet
musteri kimlik no
musteri dogum yili
musteri adres bilgileri
musteri yasi
"""

musteriadi = 'Omer Burak'
musterisoyadi = 'Goral'
musteriadsoyad = musteriadi + ' ' + musterisoyadi     # Boşluk arada 1 boşluk bırakmak için,
mustericinsiyet = True   #Erkek
musterikimlikno = '12345678911'
musteridogumyili = 1999
musteriadresi = 'Manisa Merkez'
musteriyasi = 2020 - musteridogumyili
print(musteriyasi)

"""
Siparislerin toplam bilgisini hesaplayiniz.
Siparis 1 => 110 TL
Siparis 2 => 1100.5 TL
Siparis 3 => 356.95 TL
"""

# print(110 + 1100.5 + 356.95)    #Bunu yapmak yerine değişken tanımlamalıyım.

order1 = 110
order2 = 1100.5
order3 = 356.95

print(order1 + order2 + order3) 

total = order1 + order2 + order3
print("Total", total)
