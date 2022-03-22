PYTHON NOTLARI
________________
-----------------------------------------------------------------------------------------------------------------------------------------
MANTIKSAL İŞLEMLER
___________________
ve                            # and
veya                          # or
değil                         # not
bitsel ve                     # &
bitsel veya                   # |
bitsel XOR                    # ^
bitsel sağa sola kaydırma     # << , >>
-----------------------------------------------------------------------------------------------------------------------------------------

AİTLİK OPERATÖRLERİ
_____________________
in                            -> printn("a" in "merhaba") -> true             #içerisinde belirtilen karakterin olup olmadığını denetler
not in                        -> printn("a" not in "merhaba") -> false
id()                          -> print(id(a)) ->                              #a'nın türünü söyler
is                            -> print(a is b) ->                             #a'nın b ile aynı olup olmadığını denetler   
is not                        -> print(a is not b)
-----------------------------------------------------------------------------------------------------------------------------------------

AKIŞ KONTROLÜ
_____________________
if koşul and/or koşul:
	koşula_bağlı_ifadeler
elif koşul:
	koşula_bağlı_ifadeler
else:
	koşula_bağlı_ifadeler

while:
	koşula_bağlı_ifadeler

while True:
	loopa_girecek_ifadeler

for döngü_değişkeni in üzerinde_dolaşılacak_veri:
	döngü_içi_işlemler

for sayi in range(0,10,1)
	print(sayi)

break                            # döngüleri kırıp programı sonlandırır
continue                         # mevcut döngünün sonunu getirir
pass                             # işlevi yoktur. sadece daha sonra buraya bir kod yazılacağı anlamı taşımaktadır
-----------------------------------------------------------------------------------------------------------------------------------------

LİSTELER
__________

liste = [10,20,30]               # liste isimli bir liste oluşturur
len(liste)                       # listenin uzunluğunu verir
liste[başlangıç:bitiş:artış]
liste.append(40)                 # listenin sonuna 40 verisini ekler
liste.insert(1,15)               # liste[1]'in olduğu yere 15 verisini ekler
liste.remove(20)                 # listeden 20 verisini çıkarır
a =liste.pop(2)                  # listenin 2. elemanını çıkarır
del liste[2]                     # liste[2]'nin bulunduğu yerdeki veriyi siler'
a =liste.pop()                   # listenin son elemanını listeden çıkarır ve a değişkenine atar. eğer pop(2) denirse aynını liste[2]'ye yapar
sonuc = 10 in liste              # 10 değerinin listede olup olmadığı bilgisini verir
sonuc = 10 not in liste
indis = liste.index(20)          # 20'nin liste içinde görüldüğü yeri yazar. yani Liste[1].
liste.sort()                     # listeyi küçükten büyüğe sıralar
liste.reverse()                  # listenin sırasını yersine çevirir
a = liste.count(2)               # listenin içinde kaç tane 2 girdisinin olduğunu sayar
a = max(liste)                   # listedeki en büyük elemanı verir
a = min(liste)                   # listedeki en küçük elemanı verir
a = sum(liste)                   # listedeki elemanları toplar ve sonucu verir

list1 = [1,2,3,4,5]              # zip komutu listeleri birliştirir. [(1,"a",100),(2,"b",200),(3,"c",300),(4,"d",400),(5,"e",500)] sonucu alınır
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]
print(list(zip(list1,list2,list3)))

veri = random.choice(list1)              # liste içinden bir seçim yapmak için  bu kod çalıştırılabilir.
karisik_liste = random.shuffle(list1)    # listenin içindeki verileri rastgele bir şekilde karıştırır.
veri = random.sample(list1,3)            # list1 içerisinden 3 adet veriyi rasgele çeker.

-----------------------------------------------------------------------------------------------------------------------------------------

TUPLE LAR
__________

# NOT:tupple'lar içerisinde birbirinden farklı veri tipleri saklayan listelerdir. tuple(12,true,"adam") şeklinde gösterilir.
-----------------------------------------------------------------------------------------------------------------------------------------

SET LER
_________

my_list = [1,2,2,2,1,3,4,4,5,5]
my_list = set(my_list)
print(my_list)                            # tekrar eden elemanları yok eder ve çıktı [1,2,3,4,5] şeklinde olur. set içerisinde aynı ögeler bulunmaz

-----------------------------------------------------------------------------------------------------------------------------------------

LİSTE ÜRETEÇLERİ
__________________

liste = [a for a in range(5)]                                         # [0,1,2,3,4]
liste = [a+1 for a in range(5)]                                       # [1,2,3,4,5]
liste = [a for a in range(21) if a%2==0]                              # [0,2,4,6,8,10,12,14,16,18,20]
result = [x if x%2==0 else "tek" for x in range(1,10)]                # ("tek",2,"tek",4,"tek",6,"tek",8,"tek")
-----------------------------------------------------------------------------------------------------------------------------------------

SÖZLÜKLER
___________

sozluk = {"apple":"elma" , "computer":"bilgisayar" , "book":"kitap"}  # sözlük oluşturur
sozluk["rose"] = "gül"                                                # sözlüğe "rose" ekler
del sozluk["pen"]                                                     # sözlükteki pen elemanını siler
sozluk.clear()                                                        # sözlüğü tamamen siler

users = {                                                             # bu şekilde tanımlamalar da yapılabilir
	"batuhan çabuk":{
		"age":24,
		"email":"batuhncbk@gmail.com",
		"address":"denizli"
	},
	"ezgi meriç":{
		"age":24,
		"email":"ezgimeric@gmail.com",
		"address":"eskisehir"
	}
print(users["batuhan çabuk"]["age"])                                  # users içerisindeki batuhanın age bilgisini verir
print(users["ezgi meriç"]["email"])                                   # users içerisindeki ezginin email bilgisini verir

}

sozluk = {"apple":"elma" , "computer":"bilgisayar" , "book":"kitap"}
for k in sozluk:
	print("ingilizcesi:",k,"türkçesi:",sozluk[k])

print(sozluk.items())                                                 # sozluk içindeki her iki değeri de verir

for k in sozluk.keys():                                               # anahtar değerlerini sergiler
for k in sozluk.values():                                             # değerleri sergiler

urun = {"kalem":5,"defter":10,"makas":20}
yeni = {"kalem":3,"defter":8,"makas":12,"boya":10}
urun.update(yeni)                                                     # ürün değişikliklerini gerçekleştirir

d = {"k1":1,"k2":2,"k3":3}                                            # sözlüklerde veriyi ve verinin karşılığını for döngüsünde böyle kullanmalısın
for key in d.tems():
	print(key)
-----------------------------------------------------------------------------------------------------------------------------------------

KÜMELER
_________

kume = set()
kume = {1,2,3,4}
kume.add(5)                                                           # kümeye ekleme yapar
kume.remove(2)                                                        # kumeden eleman çıkarır hata verir
kume.discard(2)                                                       # kumeden eleman çıkarır. hata vermez

kume1 = {"a","b","c"}
kume2 = {"a","b","c","d","e"}
fark = kume2.difference(kume1)                                        # kume1 ve kume2 nin arasındaki farkı verir
fark = kume2 - kume1                                                  # kume1 ve kume2 nin arasındaki farkı verir
kesisim = kume1.intersection(kume2)                                   # kume1 ve kume2 nin arasındaki kesişimi verir
kesisim = kume1&kume2                                                 # kume1 ve kume2 nin arasındaki kesişimi verir
ayrık_kume_mi = kume1.isdisjoint(kume2)                               # kesişimlerinin boş küme olup olmadığını denetler
alt_kume = kume1.issubset(kume2)                                      # altkümesi olup olmadığını denetler
kapsayan_kume = kume2.isuperset(kume1)                                # kümeyi kapsayıp kapsamadığını denetler
birlesim = kume1.union(kume2)                                         # iki kümenin birleşimini alır

studentA = ["Batu","Çabuk",1998,[70,60,70]]
studentB = ["Ezgi","Meriç",1998,[90,80,70]]
result = f"{studentA[0]} {2022 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}'dır "
print(result)
-----------------------------------------------------------------------------------------------------------------------------------------

FONKSİYONLAR
______________

name = "batuhan"
def say_hello(name):
	print("HELLO" + name)                                             # çıktı "HELLO batuhan" olacaktır.

def topla(a,b):
	sonuc=a+break
	print(sonuc)

def coklu_islem(a,b):
	topla=a+b 
	carp=a*b 
	fark=a-b
	kat=a/b 
	return topla, carp, fark, kat

k1,k2,k3,k4 = coklu_islem(5,3)                                        # bahsedildii gibi işlemlere girer ve sırasıyla değerlere atar.

def mesaj_yaz(mesaj,adet):
	for i in range(adet)
	print(mesaj)

def add(*params):                                                     # girdi olarak girilen tüm parametreleri toplar
	return sum((params))

-----------------------------------------------------------------------------------------------------------------------------------------

MATEMATİKSEL FONKSİYONLAR
___________________________

import math                                                           # matematik kütüphanesini ekler
a = math.fabs(-2)     veya           a = abs(-2)                      # mutlak'ını alır
a = math.ceil(2.015)                                                  # sayıyı yukarıya yuvarlar. sonuç 3 olur
a = math.floor(2.456)                                                 # sayıyı aşağıya yuvarlar. sonuç 2 olur
a = math.round(2.560)                                                 # sayıyı 0.5'ten büyük ve küçük olma durumuna göre yuvarlar
a = math.pow(27,1/3)                                                  # sayının üssünü alır
a = math.sqrt(25)                                                     # sayının karekökünü alır
a = math.log(1000,10)                                                 # sayının logaritmasını alır. değer 3'tür
a = math.radians(30)                                                  # dereceyi radyana çevirir
a = math.sin(30)                                                      # sayının sinüsünü alır
a = math.cos(30)                                                      # sayının cosinüsünü alır
a = math.tan(30)                                                      # sayının tanjantını alır
a = divmod(56,10)                                                     # bir sayının bir başka sayıya bölümünden, bölüm ve kalanı verir
-----------------------------------------------------------------------------------------------------------------------------------------

STRİNG FONKSİYONLARI
______________________

metin = "python güçlü bir programlama dilidir"                          
yeni_deger = metin.replace("python","PYTHON",1)                       # burada string içindeki karaklerleri değiştirir. 1 kere çalışır

yazi1 = "çiçek"
yazi2 = "ÇİÇEK"
buyuk = yazi1.upper()                                                 # yazılan harflerin her birini büyük harf olarak değiştirir
kucuk = yazi2.lower()                                                 # yazılan harflerin her birini küçük harf olarak değiştirir
metin.capitalize()                                                    # yazılan metnin sadece ilk harfini büyük gerisini küçük yapar
metin.title()                                                         # yazılan metindeki her kelimenin başını büyük yapar
metin.swapcase()                                                      # yazılan metindeki küçük harfleri büyük, büyük harfleri küçük yapar

str= "batu,ezgi"                                                      # "," lerden ayırır ve bir listeye dönüştürür
result = str.split(",")

result = " ".join(result)                                             # ayrılmış olan listeyi aralarında boşluk karakteri olacak şekilde birleştirir

yazi3 = "  programlama  "
yazi3.strip()                                                         # metnin sağındaki ve solundaki boşlukları temizler
yazi3.strip("a")                                                      # metindeki vurgulanan a karakterini siler
yazi3.lstrip("a")                                                     # soldaki a'yı siler
yazi3.rstrip("a")                                                     # sağdaki a'yı siler
yazi3.startswith("me")                                                # yazı me ile mi başlıyorun cevabı alınır
yazi3.endswith("me")                                                  # yazı me ile mi bitiyorun cevabı alınır

yazi3.count("p",0,3)                                                  # yazi3'ün içinde 0'dan 3. karaktere kadar kaç tane p var bilgisini verir
yazi3.count("p")                                                      # yazi3'ün içinde kaç tane p var bilgisini verir
yazi3.find("ama")                                                     # yazi3'ün içinde ama karakteri olup olmadığı bilgisini verir
yazi3.find("ama",0,len(yazi3))                                        # yazi3'ün içinde ama karakteri 0. karakter ile son karakter arasında olup olmadığı bilgisini verir
yazi3.isalpha()                                                       # yazi3'ün içindeki karakterlerin hepsi yazı mı
yazi3.isdigit()                                                       # yazi3'ün içindeki karakterlerin hepsi sayı mı
result= "hello".isalpha()                                             # hello kelimesinin içindeki her karakter yazı mı
result= "content".center(50," ")                                      # content kelimesinin sağına ve soluna 50 karakter boşluk ekler
result= "content".ljust(50," ")                                       # content kelimesini başa alır ve sağına 50 karakter boşluk ekler
result= "content".rjust(50," ")                                       # content kelimesini sona alır ve soluna 50 karakter boşluk ekler
result= yazi3.replace(" ","",5)                                       # yazi3'ün içindeki boşluk karakterlerinin ilk 5 tanesini siler

t = "21 nisan 2022"
gun, ay, yil = t.split()                                              # gün ay ve yıl değişkenlerinin içine boşluklara bağlı ayırıp atama işlemi gerçekleştirir.
-----------------------------------------------------------------------------------------------------------------------------------------

MODÜLLER
__________

import calendar                                                       # takvim modülü oluşturur
import time                                                           # zaman modülü oluşturur
import os                                                             # işletim sistemi modülü oluşturur
import math                                                           # matematik modülü oluşturur
import random as random_veri                                          # random_veri isimli random modülü oluşturur. x=random_veri.randint(1,50).
from math import sin, cos                                             # math modülünden sadece sin ve cos yükler. sisteme yük binmez

icerik = dir(math)                                                    # modülün altındaki tüm fonksiyonların yazılmasını sağlar
icerik = help(math)                                                   # modül hakkında detaylı anlatım sağlar
-----------------------------------------------------------------------------------------------------------------------------------------

TARİH VE ZAMAN İŞLEMLERİ
__________________________

import time                                                           # zaman modülünü ekler
print(time.time())                                                    # tick formundaki zaman bilgisini verir
guncel_zaman =time.localtime()                                        # O anki zaman verilerini getirir. guncel_zaman listesinin içine atar
zaman = time.asctime()                                                # zamanı Tue Jul 25 21:40:08 2022 formatında verir
zaman = time.strftime("%d %m %y %H:%M:%S")                            # istenilen formatta zaman bilgisini verir
""" %d rakam olarak gün bilgisi                 25
	%m iki haneli rakam olarak gün bilgisi      07
	%b üç haneli yazı olarak ay bilgisi         Jun
	%y 2 haneli yazı olarak yıl bilgisi         22
	%Y 4 haneli yazı olarak yıl bilgisi         2022
	%H Saat bilgisi                             21
	%M Dakika bilgisi                           50
	%S Saniye bilgisi                           19
	%a 3 haneli yazı ile gün bilgisi            Tue
	%A günün tam adı                            Tuesday
	%D Ay/gün/yıl                               07/25/2022     """

import calendar                                                       # takvim modülünü yükler
takvim = calendar.calendar(2022)                                      # 2022 takvimini görüntüler
takvim = calendar.month(1993,5)                                       # herhangi bir yılın herhangi bir ayını görüntüler
-----------------------------------------------------------------------------------------------------------------------------------------

HATA YAKALAMA
_______________

try:
	pass
	pass
	pass
except ValueError:
	print("girilen değer farklı")
except ZeroDivisionError:
	print("bölen sıfır olamaz")
except:
	print("farklı bir hata meydana geldi")

x = 10
if x > 5:
	raise Exception("x, 5'ten büyük değer alamaz.")

-----------------------------------------------------------------------------------------------------------------------------------------

DOSYA İŞLEMLERİ
_________________

#NOT: dosya okuma ve yazma cursorun nerede olduğuna bağlıdır.

open("dosya yolu",mod)                                 # dosya oluşturur veya var olan dosyayı açar.
r"C:\Users\Documents\deneme.txt"                       # başına r koyulması dahilinde \ özelliklerinden kaçınıldığı hatırlanmalıdır
# w: write yazma modunu açar
# a: append dosyaya veri ekleme modunu açar
# x: dosya oluşturur
# r: read dosyayı okuma modunda açar
dosya = open("deneme.txt",mode="w")                    # dosyayı veri yazma modunda oluşturur
dosya = open("deneme.txt","w")                         # dosyayı veri yazma modunda oluşturur
dosya = open("deneme.txt","w",encoding='utf-8')        # dosyayı veri yazma modunda oluşturur,içerisine yazılan neredeyse tüm karakterler(türkçe karakterler dahil) tanır
dosya.write("merhaba\n")                               # dosyaya yazı yazdırır
dosya.close()                                          # yazma bitiminde dosyayı kapatır

dosya=open("deneme.txt",mode="a")                      # dosyaya ekleme yapar
dosya.write("son bi şey daha\n")                       # dosyaya ekleme yapılacak şey yazılır
dosya.close()                                          # yazma işlemi bittiğinde dosya kapatılır

dosya=open("deneme.txt",mode="r")                      # dosyayı okuma modunda başlatır
print(dosya.read())                                    # dosyanın içinde yazan satırlar ekrana yazdırılır
dosya.read(5)                                          # dosyanın ilk 5 karakterini okur

dosya.close()                                          # dosya işlem sonrası kapatılır

dosya=open("deneme.txt",mode="r")
print(dosya.readline())                                # satır satır okuma işlemi yapar
print(dosya.readline())
print(dosya.readline())
dosya.readline(),end=""                                # okuduktan sonra otomatik koyduğu \n karakterinin sonuna end parametresini koyar ve okur.
dosya.close()

dosya=open("deneme.txt",mode="r")                      # her bir satırı tek tek for döngüsü ile okumak için bir kod dizisi
satirlar=dosya.readlines()                             # her bir satırdan bölerek bir dizi oluşturur.
for s in satirlar:
	print(s)

with open("newfile.txt","r",encoding="utf-8") as file: # dosyayı kapatmaya gerek yoktur. döngüler gibi çalışır.
	content = file.read()
	print(content)
	print(file.tell())                                     # cursorun kaçıncı karakterde olduğu bilgisini verir.
	file.seek(10)                                          # cursoru 10. konuma gönderir.

with open("newfile.txt","r+",encoding="utf-8") as file:    # hem okuma hem yazma modunda açar, güncelleme yapılacağı zaman kullanılır
	file.seek(20)
	file.write("deneme")                                   # cursoru 20. karaktere getirip oradan itibaren oradaki tüm karakterlerin yerlerini deneme karakterleri ile değiştirir.

with open("newfile.txt","r+",encoding="utf-8") as file:    # listenin ortasına veri eklemek için bu kod dizisi kullanılabilir.
	list = file.readlines()
	list.insert(1,"batu")
	file.seek(0)
	for i in list:
		file.write(i)

with open("newfile.txt","r+",encoding="utf-8") as file:    # yukarıdaki kod ile aynı işlemi yapar sadece farklı bir fonksiyon kullanıp for döngüsüne gerek duyulmaz.
	list = file.readlines()
	list.insert(1,"batu")
	file.seek(0)
	file.writelines(list)
-----------------------------------------------------------------------------------------------------------------------------------------

CLASS
_______

class Person():
	
	#class attributes
	adress = "no info"                                # global bir nesne oluşturur
	
	#constructor(yapıcı metod)
	def __init__(self,name,year,mail):                # genel veri tiplerinin saklanacağı örnek class oluşturur
	
		#object attributes
		self.name
		self.year
		self.mail

	#metods
	def intro(self):
		print("Hello there. I am " + self.name)       # class için bir metod oluşturur. self burada girilen kişinin yerine kullanılır.

	def calculate_age(self):
		return 2022 - self.year

p1 = Person("batu",1997,"batuhncbk@gmail.com")        # p1 isimli bir person klası oluşturur
p2 = Person("ezgi",1998,"ezgi17meric@gmail.com")      # p2 isimli bir person klası oluşturur
print(p1.name)                                        # p1'in name bilgisini verir
print(p2.year)                                        # p1'in year bilgisini verir
print(p1.mail)                                        # p1'in mail bilgisini verir
print(p1.adress)                                      # "no information" bilgisini verir
print(p1.intro)                                       # "hello there. I am batu" bilgisini verir
print(p1.calculate_age)                               # yaşının hesaplandığı metodu çağırır ve yaş bilgisini verir
-----------------------------------------------------------------------------------------------------------------------------------------

FONKSİYON ÖZELLİKLERİ
_______________________

def my_decorator(func):                               # fonksiyon öncesi ve sonrası işlemleri entekre edebileceğin dekoratör oluşturuyor
	def wrapper(name):
		print("fonksiyondan önceki işlemler")
		func(name)
		print("fonksiyondan sonraki işlemler")
	return wrapper

@my_decorator
def sayHello(name):
	print("hello ",name)

sayHello("batu")

def cube():                                           # yield ifadesi bellekte tutulmaz. doğrudan bir iteratöre atılır ve silinir. böylelikle ram'de veri kalabalığı oluşturmaz.
	for i in range(5000):
		yield i ** 3
generator = cube()
iterator = iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

def cube():                                           # yukarıdaki kodun aynısıdır sadece for döngüsü ile iterasyonun sonuna kadar gidilmiştir.
	for i in range(5000):
		yield i ** 3
for i in cube():
	print(i)

generator = (i**3 for i in range (5000))              # liste oluşturma metodu ile oluşturulan bir generator örneği.
for i in range generator:
	print(i)
-----------------------------------------------------------------------------------------------------------------------------------------

İLERİ SEVİYE MODÜLLER
_______________________

DATETİME MODÜLÜ                                       # zaman ile ilgili komutları kullanabileceğimiz bir modül
------------------
import datetime

simdi = datetime.now()
simdi = datetime.today()

result = datetime.now().year
resuit = simdi.year
resuit = simdi.month
resuit = simdi.day
resuit = simdi.hour
resuit = simdi.minute
resuit = simdi.second


OS MODÜLÜ                                             # işletim sistemi hakkında bilgi almak veya dosya ve klasör işlemlerinde kullanılır.
-----------
import os
os.system("notepad.exe")                              # notepad dosyasını çalıştırır.


REGULAR EXPRESSION MODÜLÜ                             # arama ve tarama işlemlerinde kullanılan bir modüldür.
-----------
import re


JSON İLE REQUESTS MODÜLÜ                             # sitelerden veri çekme işlemlerinde kullanılan bir modüldür.
-----------

import requests
import json
result = requests.get("https://jsonplaceholder.typicode.com/users")    # json dosya tipinde çözümledikten sonra istenilen veriyi ayırmak ve çekmek için kullanılır.
result = json.loads(result.text)
for i in result:
    if i["id"] == 1:
        print(i["name"])
    else:
        pass

class Github:
	def __init__(self):
		self.api_url = "https://api.github.com"
		self.token = "312739232837193782"
	def getUsers(self, username):
		response = requests.get(self.api_url+"/users/"+ username)
		return response.json()
	def getRepositories(self, username):
		response = requests.get(self.api_url+"/users/"+ username + "/repos")
		return response.json()
	def createRepositories(self, name):
		response = requests.post(self.api_url+"/user/repos?acces_token="+ self.token, json= {
			"name":name,
			"description": "this is your first repository",
			"homepage": "https://batuhncbk.com",
			"private": False,
			"has_issues": True,
			"has_projects": True,
			"has_wiki" True
		})
		return response.json()

github = Github()
while 1:
	secim = input("1 - Find User\n2 - Get Repositories\n3 - Create Repositories\n4 - Exit\nSeçim : ")
	if secim == "4":
		break
	else:
		if secim == "1":
			username = input("username = ")
			result = github.getUsers(username)
			print(f"name: {result['name']}\nPublic Repositories: {result['public_repos']}\nfollower: {result['followers']}")
		elif secim == "2":
			username = input("username = ")
			result = github.getRepositories(username)
			for repo in result:
				print(repo["name"])
		elif secim == "3":
			name = input("repository name = ")
			result = github.createRepositories(name)
			print(result)
		else:
			print("yanlış seçim")


WEB SCRAPING                                                                            # sitelerden html veri çekme işlemi.
-----------

import requests
from bs4 import BeautifulSoup                                                           # html kodları ile işlem yapmaya yarar

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"                                   # sitenin ana urlsi yazılır

html = requests.get(url).content                                                        # requests modülü ile girilen url çekilir ve içeriğe dönüştürülür
soup = BeautifulSoup(html,"html.parser")                                                # soup modülü ile html dosyası düzenlenir

list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=1)

for tr in list:
	title = tr.find("td",{"class":"titleColumn"}).find("a").text
	year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
	rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text

	print(title,year,rating)




