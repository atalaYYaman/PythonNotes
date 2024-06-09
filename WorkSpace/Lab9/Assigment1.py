#Assigment1 : Matplotlib

#matplotlib modelimizi projeye import ettik.
import matplotlib.pyplot as plt

# Veri setleri
x1 = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 10, 9, 16, 25]
x2 = [0, 1, 2, 3, 4, 5]
y2 = [0, 1, 8, 27, 64, 125]

# Grafikteki arayüz düzenlemelerini yaptık.
plt.plot(x1, y1, label='y = x^2', color='blue', linestyle='-', marker='o')
plt.plot(x2, y2, label='y = x^3', color='red', linestyle='--', marker='x')

# Grafiğin tablo ismini, yatay ve dikey ekseninin isimlerini verdik.
plt.title('Multi Line Plots')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Grafiğin sol st köşesinde gözükecek açıklama kısmını açtık
plt.legend()

# Grafiğimizi yazdırdık.
plt.show()
