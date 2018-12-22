a = int(input("birincisayi"))
b = int(input("ikincisayi"))
c = int(input("ücüncüsayi"))
d = int(input("besincisayi"))
e = int(input("altincisayi"))

dizi = [a,b,c,d,e]

dizi.sort(reverse = True)
print (dizi)
mustafa = str(dizi)
dosya = open("C:\ogrencino sonuc.txt", "w")
dosya.write(mustafa)
dosya.close()
