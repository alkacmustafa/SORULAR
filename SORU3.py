toplam = 0
dizi = []
for i in range (1001):
    islem = i ** i
    toplam += islem

print (toplam % 10000000000)
