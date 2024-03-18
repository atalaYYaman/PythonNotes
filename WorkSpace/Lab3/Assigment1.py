# Assigment 1

"""
Bir perakende mağazası için envanter yönetim sistemi geliştirdiğinizi düşünün. Anahtarların ürün adlarını ve değerlerin
stoktaki her bir ürünün miktarını temsil ettiği bir sözlüğünüz var.
"""

# Bir parakende dükkanına ait ürünler ve stock adetlerini veren dict{} tanımladık.
inventory = {
    'laptop': 50,
    'headphones': 25,
    'blender': 30,
    'microwave': 40,
    'desk lamps': 20
    }

# Example 1.1

"""
Envanter sözlüğünü ürün adlarına göre alfabetik olarak sıralayın ve görüntüleyin.
"""

# Solution 1.1

# Filtreleme yapacağımız bir fonksiyon oluşturuldu.
def filtering(inventory):

    # Dict{} içerisinde item'a göre sıralanıp listeye çevirildi.
    sortedInventory = sorted(inventory.items())

    # Listye çevirilmiş envanter tek tek yazdırıldı.
    for key, value in sortedInventory:
        print(f'{key}: {value}')

filtering(inventory)


print("\n--------------\n")

# Example 1.2

"""
Envanter sözlüğünü ürün miktarına göre artan sırada sıralayın ve görüntüleyin.
"""

# Solution 1.2

# Filtreleme yapacağımız bir fonksiyon oluşturuldu.
def filtering2(inventory):

    # Dict{} içerisinde ki itemlerın 1. elemanlarını gezerek(value değerlerini) arasında sıralama yapıldı.
    sorted_inventory = dict(sorted(inventory.items(), key=lambda item: item[1]))

    print("Sorted Inventory (by Quantity in Ascending Order):")

    # Sıralandıktan sonra listeye çevirilen envanteri tek tek yazdırdık.
    for product, quantity in sorted_inventory.items():
        print(f" {product}: {quantity}")

filtering2(inventory)


print("\n--------------\n")

# Example 1.3

"""
Envanteri yalnızca belirli bir eşikten (örneğin 30) daha az miktara sahip öğeleri görüntüleyecek şekilde filtreleyin ve 
bunları miktarlarına göre sıralayın.
"""

# Solution 1.3

# Farklı bir çözüm yöntemiyle çözülmüştür.
def filtering3(inventory):
    newInventory = []
    for i in inventory.items():
        if i[1] < 30:
            newInventory.append(i)

    for key, value in newInventory:
        print(f'{key}: {value}')

filtering3(inventory)



