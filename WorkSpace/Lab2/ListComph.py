# EXAMPLE 1

""" You are given three integers 𝑥, 𝑦 and 𝑧 representing the dimensions of a cuboid along with an integer
𝑛. Print a list of all possible coordinates given by (𝑖,𝑗, 𝑘) on a 3D grid where the sum of 𝑖 + 𝑗 + 𝑘 is
not equal to 𝑛. Here, 0 ≤ 𝑖 ≤ 𝑥; 0 ≤ 𝑗 ≤ 𝑦; 0 ≤ 𝑘 ≤ 𝑧. Please use list comprehensions rather than
multiple loops.

For example;
𝑥 = 1
𝑦 = 2
𝑧 = 2
𝑛 = 3

All permutations of [𝑖,𝑗, 𝑘] are:

[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0,
1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2]]

Print a list of the elements that do not sum to 𝒏 = 𝟑

[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]
, [1, 2, 1], [1, 2, 2]]"""

# SOLUTİON 1
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
n = int(input("Enter n: "))

output = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
print("\n>>", output)

# EXAMPLE 2
''' Given a DNA sequence represented as a string dna_sequence. Write a Python program using
dictionary comprehension to count the occurrence of each nucleotide (A, C, G, T) in the
sequence. Print the nucleotide counts in the format "Nucleotide: Count". Ensure that your code
efficiently handles sequences of varying lengths.

For example, the sample DNA sequence is "ATTGCTGACGATCGATTTCGAATCGTGG" '''

# SOLUTİON 2

dna_sequence = "ATTGCTGACGATCGATTTCGAATCGTGG"

nucleotide_counts = {nucleotide: dna_sequence.count(nucleotide) for nucleotide in "ACGT"}

print("Nucleotide counts are")
for nucleotide, count in nucleotide_counts.items():
    print(f"{nucleotide}:{count}")

# EXAMPLE 3.1
'''Write a Python program that sorts a list of tuples (that are two items) based on the absolute
difference between their elements in ascending order. (You can use abs() function.) For
example,

The given list is [(3, 7), (5, 1), (9, 6), (2, 8), (7, 5)]
The output is [(7, 5), (9, 6), (3, 7), (5, 1), (2, 8)]'''


# SOLUTİON 3.1

def getAbsolute(t):
    return abs(t[0] - t[1])


pairs = [(3, 7), (5, 1), (9, 6), (2, 8), (7, 5)]
sorted_pairs = sorted(pairs, key=getAbsolute)
print(sorted_pairs)


# EXAMPLE 3.2

"""Write a Python program that sorts a list of strings based on the number of unique characters in
each string in ascending order. For example,
The given list is ['red','indigo','green','magenta','yellow','white','lavender','orange']
The output is ['red','green','indigo','yellow','white','magenta','orange','lavender']
"""

# SOLUTİON 3.2

def getUniqueCharacterCounts(s):
    return len(set(s))

words = ['red', 'indigo', 'green', 'magenta', 'yellow', 'white', 'lavender', 'orange']
sorted_words = sorted(words, key = getUniqueCharacterCounts)
print(sorted_words)



# EXAMPLE 3.3

"""Write a Python program that sorts a list of tuples of (firstname lastname, date of birth) based
on the last name in descending order. Print the output as shown below. For example,
The given list is [("Dennis Ritchie", 1941),
 ("Alan Kay", 1940),
 ("John Backus", 1924),
 ("Ada Lovelace", 1815),
 ("John von Neumann", 1903),
 ("James Gosling", 1955)]
 """

# SOLUTİON 3.3

def sort_by_last_name_descending(lst):
    def get_last_name(name):
        return name.split()[-1]

    lst.sort(key=lambda i: get_last_name(i[0]), reverse=True)
    return lst


input_list = [("Dennis Ritchie", 1941),
              ("Alan Kay", 1940),
              ("John Backus", 1924),
              ("Ada Lovelace", 1815),
              ("John von Neumann", 1903),
              ("James Gosling", 1955)]

sorted_list = sort_by_last_name_descending(input_list)

for item in sorted_list:
    print(item)
