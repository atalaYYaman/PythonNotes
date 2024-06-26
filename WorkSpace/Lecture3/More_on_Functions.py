# DEFAULT ARGUMENT VALUES

# Bir fonksiyon tanımladık ve bu fonksiyona 3 tane parametre atadık.
# Bu parametrelerin 2'sine default(varsayılan) değerler atadık.Eğer dışarıdan değer verilmezse bu değerler kullanılacak.
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False

        retries = retries - 1

        # Eğer deneme hakkı sıfırın altına düşerse hata ver.
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# Fonksiyonu çağırırken sadece ilk parametreye(prompt) değer atadık.Diğer 2'si default(varsayılan) değer kullanacak.
ask_ok('Do you really want to quit?')

# Fonksiyonu çağırırken ilk 2 parametreye değer atadık.Sadece sonuncu parametre deafult değer kullanacak.
ask_ok('OK to overwrite the file?', 2)

# Fonksiyonu çağırıken bütün parametrelerin değerlerini verdik. Hiçbiri default değer kullanmayacak.
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

print("\n------------\n")

# Bu fonksiyonun anlamı:
#   dışardan gelen sayıları listelere ekleme;
#       eğer listede dışardan GELİRSE verilen listeye ekle
#       eğer liste dışardan GELMEZSE default(varsayılan) olarak boş bir liste oluştur ona ekle.
def f(a, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print("\n------------\n")

# Aynı fonksiyonda gelen her değeri farklı listede tutmak istiyorsak alttaki gibi yazarız.
def f(a, L=None):
    # Her fonskiyon çağrıldığında L parametresi verilmezse L listesini tekrardan empty[] listeye eşitle ve sonra ekle.
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print("\n------------\n")

#KEYWORD ARGUMENTS

# Fonksiyonu çağırırken verilen parametrelerin isimleri ve değerleri olarak karşılıklı yazılmasıdır KWARG.
#

def findvolume(length, width=1, depth=1):
    print("Length =", length)
    print("Width =", width)
    print("Depth =", depth)
    return length * width * depth

print(" 1 pozisyona göre argüman/değer(argument/value) ")
findvolume(5)

print("\n 1 keyword(anahtar kelimeye) göre argüman/değer(argument/value)")
findvolume(length=8)

print("\n 2 keyword(anahtar kelimeye) göre argüman/değer(argument/value) ")
findvolume(length=2, width=3)

print("\n 2 keyword(anahtar kelimeye) göre argüman/değer(argument/value) ")
findvolume(width=3, length=2)

print("\n 3 keyword(anahtar kelimeye) göre argüman/değer(argument/value) ")
findvolume(1, 2, 3)

print("\n 1 pozisyona göre, 1 keyword(anahtar kelimeye) göre  ")
findvolume(10, depth=4)

"""
BAZI HATALI KULLANIMLAR

findvolume() # gerekli argüman eksik.

findvolume(length=10, 5) # keyword kullandıktan sonra pozisyona göre argüman verilemez.

findvolume(20, length=10) # aynı argüman için birden fazla değer verilemez.

findvolume(height=10) # olmayan argümana değer verilemez.

"""

print("\n------------\n")

# Bu fonksiyonda 3 farklı türde parametre kullanıldı:
#   1) Pozisyona göre argüman
#   2) Kullanacağımız parametrenin önüne "*" getirerek birden fazla argümanı value olarak isteyebiliyoruz.
#   3) Kullanacağımız parametrenin önüne "**" getirerek birden fazla argümanı key=value olarak isteyebiliyoruz.

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.",
shopkeeper="Michael Palin",
client="John Cleese",
sketch="Cheese Shop Sketch")


#EXAMPLE

def example_function(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

example_function(1, 2, 3, name="Alice", age=30, city="New York")

print("\n------------\n")

# RECURSİON (özyineleme)

"""
- Özyineleme, bir fonksiyonun kendi kendini çağırdığı bir programlama kavramıdır.
- Özyineleme tipik olarak, tıpkı orijinal problem gibi olan ancak çözülmeye bir adım daha yakın olan alt problemlere
 ayrıştırılabilen problemleri çözmek için kullanılır.
 """
# Bu fonksiyonda verilen pozitif sayıların 1'e  eşit olasıya kadar 1 azaltıldığı RECURSİON fonksiyondur.
def f(n):
    if n == 1:
        return 1
    else:
        return f(n - 1)


f(2)
f(3)

# Computation

"""
- Tüm hesaplamalar durumdan duruma geçmekten ibarettir...
- Mevcut durum göz önüne alındığında, bir sonraki duruma hangi durumda geçeceğimizi söyleyen bir dizi kural vardır.
"""

# Piecewise Functions
"""
f(n) = 1 if n = 1
n - 1 if n > 1
f(4)
4 - 1
3
"""

# Yukarıdaki fonksiyonun pythonada gösterimi

def ff(n):
    if n == 1:
        return 1
    else:
        return n - 1

# Fancier Functions
# İç içe fonksiyonlar kullandık g() fonksiyonu çağırdığımızda f() fonksiyonuda beraberinde geliyor.

def fff(n):
    return n + (n - 1)

def g(n):
    return n + fff(n - 1)

g(4)

print("\n------------\n")

# Iterative algorithms
"""
- Döngü yapıları (örn. while veya for döngüleri) doğal olarak yinelemeli algoritmalara yol açar.
- Döngü boyunca her iterasyonda güncellenen bir dizi "durum değişkeninde" hesaplamayı yakalamak olarak 
kavramsallaştırılabilir.
"""

# Alttaki fonksiyonda ilk parametre toplanacak olan sayıyı ikincisi kaç defa toplanacağına karar veriyor.
def iterMul(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

print(iterMul(2, 3))