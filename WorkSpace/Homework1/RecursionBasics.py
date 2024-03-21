# What is Recursion

def factorial(n):
  if n==1:
    return 1
  else:
    return n*factorial(n-1)

print(factorial(5))

# Reading Question 1

# Under what circumstances does it make sense to use recursion?
"""
A) Recursion can be used at any time

(True)B) Recursion works best when the solution is self-similar

C) Recursion is too hard; avoid it at all costs

D) Recursion only works with mathematical concepts like factorial and the Fibonacci sequence
"""

print("\n---------------------\n")

# Fibonacci Sequence

def fibonacci(n):
    """Calculate Fibonacci numbers"""
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))


fibonacci_length = 10
for num in range(fibonacci_length):
    print(fibonacci(num))

# Reading Question 2

# What is the purpose of the base case in recursion?

"""
The base case tells the function to call itself.

The base case is another name for recursion.

The base case is the name of the recursive function.

(True) When true, the base case stops the recursive calls and returns a value.
"""

print("\n---------------------\n")

# Formative Assesment

"""
Rearrange the code blocks below to create a recursive function that finds the sum of n integers. For example, 
find_sum(5) would add up the numbers 0 to 5.
"""

def find_sum(n):
    if n == 0:
        return 0
    else:
        return (n + find_sum(n-1))

print(find_sum(5))