import pandas as pd

# Population dataframe dosyasını oku
df = pd.read_csv('population_data.csv')
print("DataFrame:")
print(df)

# 'Ülke' adının 'T' harfiyle başladığı satırları filtrele
df_t_countries = df[df['Country'].str.startswith('T')]
print("\nCountries starting with 'T':")
print(df_t_countries)

# 'Kıta'nın 'Asya' olduğu satırları filtreleyin
df_asia = df[df['Continent'] == 'Asia']
print("\nCountries in Asia:")
print(df_asia)

# Nüfus yoğunluğunu hesaplamak için özel bir fonksiyon tanımlama
def calculate_nufus_yogunlugu(row):
    return row['Population'] / row['Area_km2']


# Yeni bir 'nufus_yogunlugu' sütunu oluşturmak için işlevi uygulayın
df['nufus_yogunlugu'] = df.apply(calculate_nufus_yogunlugu, axis=1)
print("\nDataFrame with 'nufus_yogunlugu' column:")
print(df)


# Azalan sırada 'Nüfus' sütununa göre sırala
df_sorted_by_population = df.sort_values(by='Population', ascending=False)
print("\nDataFrame sorted by 'Population' in descending order:")
print(df_sorted_by_population)

# 'Nüfus_Yoğunluğu' sütununa göre artan sırada sırala
df_sorted_by_density = df.sort_values(by='nufus_yogunlugu', ascending=True)
print("\nDataFrame sorted by 'Population_Density' in ascending order:")
print(df_sorted_by_density)


# 'Kıtaya' göre gruplayın ve her kıta için toplam nüfusu hesaplayın
continent_population = df.groupby('Continent')['Population'].sum().reset_index()
print("\nTotal population for each continent:")
print(continent_population)


# DataFrame'in ilk 10 satırını görüntüle
print("\nFirst 10 rows of the DataFrame:")
print(df.head(10))


# DataFrame'in son 10 satırını görüntüle
print("\nLast 10 rows of the DataFrame:")
print(df.tail(10))

