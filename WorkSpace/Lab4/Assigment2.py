#example2
def merge(lst1,lst2):
    if len(lst1)==0 and len(lst2)==0:
        return 0
    else:
        return lst1 + lst2
print(merge([1, 5, 8], [2, 7, 9, 10]))
print(merge([1, 2, 3], []))