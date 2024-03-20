# Assigment 3

"""
Üç liste oluşturun: sırasıyla öğrencilerin adlarını, öğrenci kimliklerini ve notlarını içeren names, student_ids ve
grades. Bu listeleri aynı anda yinelemek için zip() işlevini kullanın ve her öğrencinin bilgilerini şu biçimde yazdırın:
 "İsim: <name>, Öğrenci Kimliği: <student_id>, Grade: <not>" biçiminde yazdırın.
"""

# Öğrencilere ait bilgiler tanımlandı.
names = ("Ali","Veli","Ahmet","Ayşe")
ids = (1,2,3,4)
grades = (85,95,90,70)

# Bütün öğrenci bilgileri önce ziplenip sonrasında tuple içerisine alındı.
holdStudent = tuple(zip(names, ids, grades))

# Ziplenmiş tuple'ı(holdStudent) for döngüsüyle yazdırıldı.
for name, id, grade in holdStudent:
    print(f"İsim: {name} Öğrenci no: {id} Not: {grade}")