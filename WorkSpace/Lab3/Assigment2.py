# Assigment 2

"""
İki sayı listesi alan ve verilen listelerdeki öğelerin ikili karşılaştırmalarının sonucunu içeren yeni bir liste
döndüren bir Python işlevi yazın (örneğin, daha büyük, daha küçük veya eşit).
"""

# Solution

# Karşılaştırmada kullanmak için 2 liste belirlendi.
list1 = [1, 3, 5, 6, 9]
list2 = [2, 3, 4, 10, 1]


def compare(list1, list2):

    # Karşılaştırdıktan sonra sembollerin ekleneceği boş liste.
    symbolList = []

    # İki listenin elemanlarınıda gezmek için listeler ziplenip sonrasında for döngüsüyle gezilir.
    for x, y in zip(list1,list2):
        if x == y:
            symbolList.append("=")
        elif x < y:
            symbolList.append("<")
        elif x > y:
            symbolList.append(">")
    print(symbolList)

compare(list1, list2)