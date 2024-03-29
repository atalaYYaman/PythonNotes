# Assigment 1.1: Falling Factorial (Iterable method)
"""
Write an iterative function falling_iterative, which is a "falling" factorial that takes two
arguments, n and k, and returns the product of k consecutive numbers, starting from n and
working downwards. When k is 0, the function should return 1.
"""

# Solution
# Iterable method'larda fonksiyon tek bir defa çağırılır ve kendi içerisinde tekrar eder.

def falling_iterative(n, k):
    result = 1
    for i in range(k):
        result *= n
        n -= 1
    return result
print(falling_iterative(6, 3))
print(falling_iterative(10, 0))
print("===================================")

# Assigment 1.2: Falling Factorial (Recursive method)
"""
Write a recursive function falling_recursive, which is a "falling" factorial that takes two
arguments, n and k, and returns the product of k consecutive numbers, starting from n and
working downwards. When k is 0, the function should return 1.
"""

# Solution
# Recursive method'larda fonksiyonun içerisinde fonksiyon tekrar çağırılır buna da özyineleme denir.

def falling_iterative(n,k):
    if k==0:
        return 1
    else:
        return n * falling_iterative(n-1,k-1)
print(falling_iterative(6, 3))
print(falling_iterative(10, 0))
