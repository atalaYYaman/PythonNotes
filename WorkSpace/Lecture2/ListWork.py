#LİST COMPREHENSİONS
num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_numbers = []
for number in num_lst:
    squared_numbers.append(number**2)
print(squared_numbers)
#aynı işlemin daha kısa hali
print("---------------------")
squared_numbers = [number ** 2 for number in num_lst]
print(squared_numbers)
print("---------------------")
#----------------------------
#Büyük karakterleri küçüğe çevirme
random_case = ["Hi","mOm","aND"]
all_lower = []
for word in random_case:
    all_lower.append(word.lower())
print(all_lower)
print("---------------------")
#tek satırda yazılmış hali
all_lower2 = [case.lower() for case in random_case]
print(all_lower2)
print("---------------------")
#----------------------------
#Listenin içerisinde tuple kullanma
words = ["I","love","python"]
result = []
for word in words:
    result.append((word, len(word)))
print(result)
print("---------------------")
#List comperation ile kısaltılmış hali
result=[(word, len(word)) for word in words]
print(result)
print("---------------------")
#-------------------
#Celcius'u fahren.. a çevirme
temps_c = [15,16,17,8,9,10,100]
temps_f =[]
for t in temps_c:
    conversion_result = t*(9/5)+32
    temps_f.append(conversion_result)
print(temps_c)
print(temps_f)
print("---------------------")
#List comperation
result = [t*(9/5)+32 for t in temps_c]
print(result)
print("---------------------")
#Fonksiyon kullanalarak yapılmış hali
def c_to_f(t):
    return t*(9/5)+32
result = [c_to_f(t) for t in temps_c]
print(result)
print("---------------------")
#----------------------------
#Soyisimleri ayırıp gruplamak için,
names = ["John Ritchie","Smith Kay","Alan Backus"]
print("Last Names:")
for n in names:
    print(n.split(" ")[-1])
print("---------------------")
#--------------------------
#listedeki sayıları stringe çevirme
my_numbers = [15,67,99,25,14]
newlist = ["hello" for x in my_numbers]
print(newlist)
print("---------------------")
#---------------------
#Listede ki çift sayıları bulmak için,
nums = [12,13,14,15,16,17,18,19,20]
even_numbers = []
for number in nums:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)
print("---------------------")
#List compera... ile tek satırda yazımı
even_numbers = [number for number in nums if number % 2 ==0]
print(even_numbers)
print("---------------------")
#Listede isimi "y" ile bitenler
kids = ["jonathan","james","henry","audrey","juliette"]
end_kids_y = []
for kid in kids:
    if kid.endswith("y"):
        end_kids_y.append(kid)
print(end_kids_y)
print("---------------------")
#List compe... ile tek satırda yazımı
result = [name for name in kids if name.endswith("y")]
print(result)
print("---------------------")
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]
]
a = [[row[i] for row in matrix] for i in range(4)]
print(a)
print("---------------------")
mydict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Extracting a subset of the dictionary based on some condition
subset_dict = {key : value for key, value in mydict.items() if  value %3 == 0}
print(subset_dict)
print("---------------------")
words = ["apple", "banana", "cherry", "pear"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)
print("---------------------")
num_lst = [3, 4, 5, 8, 1, 12.3, 0, -3]
sorted_lst = sorted(num_lst)
print(sorted_lst)
# sorted_lst → [-3, 0, 1, 3, 4, 5, 8, 12.3]
rev_sorted_lst = sorted(num_lst, reverse=True)
print(rev_sorted_lst)
# rev_sorted_lst → [12.3, 8, 5, 4, 3, 1, 0, -3]


def lastCharacter(value):
    return value[-1]
def numberOfVowels(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    total = 0
    for vowel in vowels:
        total += word.count(vowel)
    return total

def main():
    ## Custom sort a list of words.
    list1 = ["python", "cat", "equals", "one", "break", "two"]
    list1.sort(key=len)
    print("Sorted by length in ascending order:")
    print(list1, '\n')
    list1.sort(key=lastCharacter)
    print("Sorted by last character in ascending order:")
    print(list1, '\n')
    list1.sort(key=numberOfVowels, reverse=True)
    print("Sorted by number of vowels in descending order:")
    print(list1)

main()
print("---------------------")
names = ["Dennis Ritchie", "Alan Kay", "John Backus", "James Gosling"]
names.sort(key=lambda name: name.split()[-1])
nameString = ", ".join(names)
print(nameString)

#SORTING DICTIONARİES
my_dict = {'banana': 3, 'apple': 1, 'orange': 2}

# sorting by keys
sorted_dict_by_keys = dict(sorted(my_dict.items()))
print(sorted_dict_by_keys)

# sorting by values
sorted_dict_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict_by_values)

print("------------------------------- \n")

#EXERCİSE
students_grades = {
'Ali': 85,
'Ahmet': 70,
'Zeynep': 95,
'Ayşe': 60,
'Can': 75
}

def sorting(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    for student, grade in sorted_dict:
        print(f"{student}: {grade}")
print("Students sorted by grades in descending order:")
sorting(students_grades)

print("------------------------------- \n")

meals = ('breakfast', 'lunch', 'dinner')
meal_times = ('8 am', '12 pm', '6 pm')
meal_info = tuple(zip(meals, meal_times))
print(meal_info)