#Assigment2
#Iterators and Generators
#Task1

#Bir birden fazla obje üzerinden çalışabilmek için classımızı açtık.
class FilterIterator:

    def __init__(self, iterable, func):
        self.iterable = iterable
        self.func = func
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.iterable):
            value = self.iterable[self.index]
            self.index += 1
            if self.func(value):
                return value
        raise StopIteration

#FilterIterator içerisinde func yerine geçer ve sayının pozitifliğini kontrol eder.
def is_positive(x):
    return x > 0


numbers = [6, 5, -2, 8, -9, -3, 7]
filtered_iterator = FilterIterator(numbers, is_positive)
for num in filtered_iterator:
    print(num)
