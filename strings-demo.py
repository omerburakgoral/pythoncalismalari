website = "https://www.omerburakgoral.com"
course = "Ben Kimim? Neler Yaptım? Baştan sona hayatım."
#1 'course' dizisi içinde kaç karakter bulunmaktadır.
#2 'website' içinden www karakterlerini alın.
#3 'website' içinden com karakterlerini alın
#4 'course' içinden ilk 10 ve son 10 karakterleri alın
#5 'course' ifadesindeki karakterleri tersten yazdırın.

name, surname, age, job = 'Ömer Burak', 'Göral', 22, 'Öğrenci'

#6  Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#   'Benim adım Ömer Burak Göral, yaşım 22 ve mesliğim öğrenci.'
#7  'Hello world' ifadesindeki 'w' harfini 'W' ile değiştirin.
#8  'abc' ifadesini yan yana 3 defa yazdırın.

result = len(course) #1.soru-----------------------------------------------------

print(result)

result = website[8:11] #2. soru--------------------------------------------------
print(result)

result = website[27:30] #3. soru-------------------------------------------------
print(result)

lenght = len(website)  # bu da 2. yol
result = website[lenght-3:lenght]
print(result)

result = course[:10]  #4. soru---------------------------------------------------
print(result)
result = course[-10:] ## sona -1 deseydik son karakteri almayacaktı o yüden : sonra bıraktık ki sonuna kadar alsın.
print(result)

result = course[::-1] ##[::2] 2 karakterde 1 alır. [::3] 3 karakterde 1 alır. #5.soru----------------------------------------------
print(result)

result = (f"Benim adım {name} {surname},yaşım {age} ve mesleğim {job}")    #6.soru---------------------------------------------------
print(result)

result = "Benim adım " + name+ " " + surname+ ",yaşım " +str(age)+ " ve mesleğim "+ job  ##bu da 2. yol ama sayıyı str çevirmeyi unutma.
print(result)

result = ("Benim adım {} {},yaşım {} ve mesleğim {}".format(name, surname, age, job))   ## bu da 3. yol. direkt f kullanmak daha basit ama duruma göre bunu da kullanabilirsin.
print(result)

kelime = "Hello world"   #7.soru-------------------------------------------------
kelime = kelime[:6] + 'W' + kelime[-4:]
print(kelime)

result = 'abc ' * 3
print(result)

