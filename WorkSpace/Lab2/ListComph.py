#EXAPMLE 1
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
n = int(input("Enter n: "))

output = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]

#EXAPMLE 2

Dna = "ATTGCTGACGATCGATTTCGAATCGTGG"
dna_char = ["A","T","C","G"]
totalA = 0
totalT = 0
totalC = 0
totalG = 0

result = [a.count(b) for a in Dna for b in dna_char]
print(result)

#EXAMPLE 3.1
nums = [(3, 7), (5, 1), (9, 6), (2, 8), (7, 5)]
result = []

#EXAMPLE 3.2
def sort_by_unique_chars(lst):
    # Define a custom sorting function based on the number of unique characters
    def unique_chars_count(string):
        return len(set(string))

    # Sort the list based on the number of unique characters using the custom sorting function
    lst.sort(key=unique_chars_count)
    return lst

# Test the function
input_list = ['red', 'indigo', 'green', 'magenta', 'yellow', 'white', 'lavender', 'orange']
sorted_list = sort_by_unique_chars(input_list)
print(sorted_list)

#EXAMPLE 3.3
def sort_by_last_name_descending(lst):
    def get_last_name(name):
        return name.split()[-1]

    lst.sort(key=lambda x: get_last_name(x[0]), reverse=True)
    return lst

input_list = [("Dennis Ritchie", 1941),
              ("Alan Kay", 1940),
              ("John Backus", 1924),
              ("Ada Lovelace", 1815),
              ("John von Neumann", 1903),
              ("James Gosling", 1955)]

sorted_list = sort_by_last_name_descending(input_list)

# Print the output
for item in sorted_list:
    print(item)
