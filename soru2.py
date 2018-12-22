m = input("cümle")
print(m[::-1])
print(m.split(" "))
harfler = []
sayisi = []
for i in(m):
    if not (i in harfler):
        harfler.append(i)
        sayisi.append(1)
    else:
        sayisi[harfler.index(i)] = sayisi[harfler.index(i)]+1
print("kaç harf var;")
for j in range (len(harfler)):
    print(harfler[j],"'den",sayisi[j],"tane")
tersten = m[::-1]
ayrıayrı = tersten.split(" ")
print("ters çevrilmiş hali:",ayrıayrı[::-1])
unluler = ["a","e","o","ö","u","ü","ı","i"]
unlu = []
unsuz = []
for i in range m:
    if i == unluler[0]or i == unluler[1]or i == unluler[2]or i == unluler[3]or i == unluler[4]or i == unluler [5]or i == unluler[6]or i == unluler[7]:
        unlu.append(i)
    else:
        unsuz.append(i)
print("ünlüharfler",unlu)
print("unsuzharfler", unsuz)
duzunlu = ["a","e","ı","i"]
yuvarlakunlu = ['o','ö','u','ü']
_yuvarlaktansonragelmeyen = ['ı','i','o','ö']
sesliharfler = ['a','e','ı','i','o','ö','u','ü']
sesliharfler_ = []
uyuyormu = True
duzmu = False
yuvarlakmi = False

print("Bir kelime giriniz : ")
kelime = input()

for i in range(0,len(kelime)):
  if kelime[i] in duzunlu:
    duzmu = True
    break
  elif kelime[i] in yuvarlakunlu:
    yuvarlakmi = True
    break

for i in range(0,len(kelime)):
  if kelime[i] in sesliharfler:
    sesliharfler_.append(kelime[i])

for i in range(0,len(sesliharfler_)):
  if duzmu == True and sesliharfler_[i] in yuvarlakunlu:
    uyuyormu = False
  if yuvarlakmi == True and sesliharfler_[i] in _yuvarlaktansonragelmeyen:
    uyuyormu = False

if uyuyormu == False:
  print("Küçük Ünlü Uyumuna Uymuyor")
elif uyuyormu == True:
  print("Küçük Ünlü Uyumuna Uyuyor")

