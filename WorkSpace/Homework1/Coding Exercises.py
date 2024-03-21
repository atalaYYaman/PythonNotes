# Recursion Exercise 1

"""
Write a recursive function called recursive_sum that takes an integer as a parameter. Return the sum of all integers
between 0 and the number passed to recursive_sum.
"""

#Solution

def recursive_sum(number):
    if number == 0:
        return 0
    else:
        return number + recursive_sum(number - 1)

print(recursive_sum(5))

print("\n------------\n")

# Recursion Exercise 2

"""
Write a recursive function called list_sum that takes a list of numbers as a parameter. Return the sum of all of the 
numbers in the list.
"""

#Solution

def list_sum(numbers):
    if numbers == []:
        return 0
    else:
        return numbers[0] + list_sum(numbers[1:])

print(list_sum([10,12.5,10,7]))

print("\n------------\n")

# Recursion Exercise 3

"""
Write a recursive function called bunny_ears that takes the number of bunnies (an integer) as a parameter. Return the
number of bunny ears (2 per bunny). Do not use multiplication; instead use addition.
"""

# Solution

def bunny_ears(num_bunnies):
    if num_bunnies == 0:
        return 0
    else:
        return 2 + bunny_ears(num_bunnies - 1)

print(bunny_ears(2))


print("\n------------\n")


# Recursion Exercise 4
"""
Write a recursive function called reverse_string that takes a string as a parameter. Return the string in reverse order.
Hint, the slice operator will be helpful when solving this problem.
"""

# Solution

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


print(reverse_string("cart"))

print("\n------------\n")

# Recursion Exercise 5

"""
Write a recursive function called get_max that takes a list of numbers as a parameter.
Return the largest number in the list.
"""

# Solution

def get_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], get_max(lst[1:]))

print(get_max([11, 22, 3, 41, 15]))