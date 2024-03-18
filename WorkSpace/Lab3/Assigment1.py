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



