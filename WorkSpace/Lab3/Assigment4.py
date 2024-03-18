def filter_numbers(*numberList, **kwargs):
    divisor = kwargs.get('divisor', 1)
    return [num for num in numberList if num % divisor == 0]

result1 = filter_numbers(1,2,3,4,5,6, divisor = 3)
print(result1)

result2 = filter_numbers(10,20,30,40,50)
print(result2)

result3 = filter_numbers(3, 6, 9, 12, 15, divisor=5)
print(result3)

