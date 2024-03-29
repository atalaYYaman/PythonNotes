# Assignment 2: Merge
"""
Write a recursive function merge that takes 2 sorted lists lst1 and lst2, and returns a new
list that contains all the elements in the two lists in sorted order.
Hint: Remember to concatenate two lists using '+' operator, e.g. [7] + [9] = [7, 9]
"""


def merge(lst1, lst2):
    # Iterable method: Listelerden biri boşsa, diğer listeyi döndür
    if not lst1:
        return lst2
    if not lst2:
        return lst1

    # Recursive method: İki listenin ilk öğelerini karşılaştırın
    if lst1[0] < lst2[0]:
        # lst1'in ilk öğesi daha küçükse, bunu sonuca ekleyin ve lst1 ile lst2'nin geri kalanını özyinelemeli
        # olarak birleştirin
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        # lst2'nin ilk öğesi daha küçük veya eşitse, bunu sonuca ekleyin ve lst1 ile lst2'nin geri kalanını özyinelemeli
        # olarak birleştirin
        return [lst2[0]] + merge(lst1, lst2[1:])


print(merge([1, 3, 5], [2, 4, 6]))  # Çıktı: [1, 2, 3, 4, 5, 6]
print(merge([1, 4, 7], [2, 3, 9]))  # Çıktı: [1, 2, 3, 4, 7, 9]
