inventory = {
    'laptop': 50,
    'headphones': 25,
    'blender': 30,
    'microwave': 40,
    'desk lamps': 20
    }
def filtering(inventory):
    sortedInventory = sorted(inventory.items())
    for key, value in sortedInventory:
        print(f'{key}: {value}')

filtering(inventory)

print("\n--------------\n")

def filtering2(inventory):
    newInventory = []
    for i in inventory.items():
        newInventory.append(i)

    newInventory.sort(key=lambda x: x[1])
    for key, value in newInventory:
        print(f'{key}: {value}')

filtering2(inventory)

print("\n--------------\n")

def filtering3(inventory):
    newInventory = []
    for i in inventory.items():
        if i[1] < 30:
            newInventory.append(i)

    for key, value in newInventory:
        print(f'{key}: {value}')

filtering3(inventory)

print("\n--------------\n")

list1 = [1, 3, 5, 6, 9]
list2 = [2, 3, 4, 10, 1]

def compare(list1, list2):
    symbolList = []
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            symbolList.append("=")
        elif list1[i] < list2[i]:
            symbolList.append("<")
        elif list1[i] > list2[i]:
            symbolList.append(">")
    print(symbolList)

compare(list1, list2)