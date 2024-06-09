#Assigment1

import pandas as pd

# (a) DataFrame'i oluştur.
data = {
    'Product': ['apple', 'banana', 'potato', 'orange', 'broccoli', 'spinach', 'cherry'],
    'Price': [25, 30, 10, 35, 40, 15, 25],
    'Quantity': [18, 25, 30, 7, 5, 12, 21],
    'Category': ['Fruit', 'Fruit', 'Vegetable', 'Fruit', 'Vegetable', 'Vegetable', 'Fruit']
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# (b) Verileri indeksle ve seç.
print("\n'Category' column:")
print(df['Category'])

print("\nRows where 'Quantity' is greater than 20:")
print(df[df['Quantity'] > 20])

print("\nRow where 'Product' is 'orange':")
print(df[df['Product'] == 'orange'])

# (c) Yeni bir 'Toplam Fiyat' sütunu ekle
df['Total Price'] = df['Price'] * df['Quantity']
print("\nDataFrame with 'Total Price' column:")
print(df)

# (d) Tüm ürünlerin ortalama fiyatını hesaplayın ve görüntüle
average_price = df['Price'].mean()
print("\nAverage price of all products:")
print(average_price)

# (e)'Meyve' kategorisine ait olan ve 'Toplam Fiyatı' 250'den fazla olan ürünleri filtrele ve görüntüle
filtered_df = df[(df['Category'] == 'Fruit') & (df['Total Price'] > 250)]
print("\nFiltered products (Fruit category with 'Total Price' > 250):")
print(filtered_df)
