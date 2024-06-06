'''
Create a Module
    "
        def greeting(name):
            print(f"Hello {name}")
    "
-Bu kod dosyasını example.py olarak kaydet.
'''


'''
Importing Modules
-Import komuduyla birlikte uzantısı(.py) olmadan projeye eklenir.
    "
        import example
    "

-Erişimi kolaylaştırmak için, modülün içindeki fonksiyona erişmenin yolu.
    "
        from example import greeting
    "     
    
'''


'''
 Modülün içindeki Değerler - Variables in Module
    
-Aşağıdaki kod satırını example.py olarak kaydet.
    "
        person = {
            "name": "Ali",
            "age": 25
            }
    "
-Modülün içindeki değerler yazdırılabilir.Aşağıdaki kod satırını çıktısı 25 olacak.
    "
        import example
        
        a= example.person["age"]
        print(a)
    "
       
'''


'''
Modülleri adlandırlabiliriz.
-Aşağıda example modülü kod içerisinde kullanılmak için ex olarak adlandırılıyor.
    
    "
        import example as ex
        
        a= ex.person["age"]
        print(a)
    "
 
'''

'''
Modülleri script olarak çağırabilir ve işlem yaptırabiliriz.

Ama eğer modülümüzün içinde alttaki gibi bir kontrol sorgusu kullandıysak.
Normalde direk sonucu yazdırırken artık import sonrasında fonksiyonunda çağrılmasını isteyecektir.

    "
        if __name__ == "__main__":
    "
    
'''

'''
sys modülü,
    Python'daki sys modülü, Python çalışma zamanı ortamının farklı bölümlerini manipüle etmek için kullanılan çeşitli 
    işlevler ve değişkenler sağlar. Yorumlayıcı ile güçlü bir şekilde etkileşime giren değişkenlere ve işlevlere erişim
    sağladığı için yorumlayıcı üzerinde çalışmaya izin verir.
'''

import sys
# Burada sys modülünü importladıktan sonra içerisinde bir fonksiynu kullanarak bazı işlemler gerçekleştiriyoruz.
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")


'''
Modülümüzde ki fonksiyonları(ya da değişken isimlerini),
"dir()" kullanarak yazdırabiliriz. 
'''
print(dir(sys))


'''
Bazı faydalı modüller;
– random
– statistics
– datetime
– glob
– os
'''


'''
RANDOM modülü
-Bu modül çeşitli dağılımlar için sözde rasgele sayı üreteçleri uygular.

'''

import random

#Bu choıce fonksiyonu verilen değerlerden rastgele birini seçer.
coin = random.choice(["heads", "tails"])
print(coin)

#Bu randint fonksiyonu verilen 2 değer arasında rastgele bir sayı seçer.
number = random.randint(1, 10)
print(number)

#Bu shuffle fonksiyonu verilen listedeki değerlerin sıralamasını rastgele karıştırır.
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)


'''
Statistics modülü,
-Bu modül, sayısal verilerin matematiksel istatistiklerini hesaplamak için fonksiyonlar sağlar.

'''
import statistics

#Bu mean fonksiyonu verilen değerlerin ortalaması hesaplıyor.
print(statistics.mean([100, 90]))


'''
datetime modülü,
Zaman damgaları içeren bir veri kümesi üzerinde çalışıyorsanız, datetime modülü 
zaman damgasından bilgi ayrıştırmak için kullanışlıdır.

'''
import datetime


'''
glop modülü,
Adında bir tür kalıp paylaşan bir grup dosyayı ayrıştırmak istiyorsanız, glob bunu kolaylaştırır.    

'''
import glob

# * her şeyle eşleşir;
# *.txt tüm .txt dosyalarıyla eşleşir;
# *abc* adında abc geçen tüm dosyalarla eşleşir.
files = glob.glob("path/to/files/*.txt")
for file in files:
    f = open(file, "r")


'''
Os modülü,
bilgisayarınızın işletim sistemiyle doğrudan etkileşim kurmanızı sağlar. 
İşletim sistemi, hangi programın işlemci üzerinde çalışacağına karar vermek ve verilerin bellekte nerede saklanacağına 
karar vermek gibi düşük seviyeli işlemleri yöneten bilgisayarın bir parçasıdır.

Aşağıdaki işlevler özellikle kullanışlıdır:

os.listdir(path) # dizindeki dosyaların bir listesini döndürür
os.path.exists(path) # verilen yol mevcutsa True döndürür
os.rename(a, b) # a dosyasının adını b olarak değiştirir
os.remove(path) # dosyayı siler.
# UYARI: program aracılığıyla silme kalıcıdır!
'''


'''
pip modülü,
Modülleri manuel olarak yüklemek genellikle mümkündür, ancak bu işlem büyük bir acı olabilir. 
Neyse ki, Python bize modülleri yüklemek için kolaylaştırılmış bir yaklaşım sunuyor - pip modülü! 
Bu özellik Python Paket İndeksi'nde (yaygın olarak kullanılan modüllerin bir listesi) indekslenen modülleri bulabilir,
indirebilir ve yüklemeyi deneyebilir.

Terminalde pip çalıştırmak için şu komutu kullanın:
pip install modül-adı
'''