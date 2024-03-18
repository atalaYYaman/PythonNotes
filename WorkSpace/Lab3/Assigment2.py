list1 = [1, 3, 5, 6, 9]
list2 = [2, 3, 4, 10, 1]

def compare(list1, list2):
    symbolList = []
    for x, y in zip(list1,list2):
        if x == y:
            symbolList.append("=")
        elif x < y:
            symbolList.append("<")
        elif x > y:
            symbolList.append(">")
    print(symbolList)

compare(list1, list2)