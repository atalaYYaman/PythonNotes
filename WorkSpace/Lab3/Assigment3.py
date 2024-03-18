names = ("Ali","Veli","Ahmet","Ayşe")
ids = (1,2,3,4)
grades = (85,95,90,70)

holdStudent = tuple(zip(names, ids, grades))
for name, id, grade in holdStudent:
    print(f"İsim: {name} Öğrenci no: {id} Not: {grade}")