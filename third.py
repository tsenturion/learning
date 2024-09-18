from cProfile import label


def sqr1(number):
    return number * number

def printf(some_list, func):
    for i in some_list:
        print(func(i))


list1 = list(range(5))

printf(list1, sqr1)
printf(list1, lambda x : x * x)


sqr = lambda x : x * x + 5

print(sqr(5))

for i in map(sqr1, list1):
    print(i)

list2 = list(map(sqr1, list1))
print(list2)

for i in filter(lambda x : x % 2 == 0, list1):
    print(i)

fib = lambda n : n if n <= 1 else fib(n - 1) + fib(n - 2)
fact = lambda n : 1 if n == 0 else n * fact(n - 1)

#vfact = lambda f: f(f, n)
#infact = lambda n :
fact2 = lambda f , x :  1 if x == 0 else x * f(f, x - 1)
ifact = lambda n : (lambda f: f(f, n))(fact2)

list1 = list(map(fib, range(10)))
list2 = list(map(fact, range(10)))
print(list1)
print(list2)

strlist = ['fsd1231', 'fsd1231', 'fsd1231', 'fsd1231']
"""сделать первые буквы заглавными map, lambda"""

strlist = list(map(lambda n : n.title(), strlist))

numlist = ['1 2 3 4', '1 2 3 4', '1 2 3 4', '1 2 3 4']
"""найти сумму элементов map, lambda, .split()numlist = [10, 10, 10, 10]"""
numlist = list(map(lambda s: sum(map(int, s.split())), numlist))

strlist = ['121', 'fsd1231', 'fsd1231', 'Rsd1231', 'Rsd1231']
"""список слов с заглавной буквы, сделать их прописными filter
strlist = ['rsd1231', 'rsd1231']"""
strlist = list(map(lambda x : x.lower(), ))

strlist = ['121', '123321', 'fsd1231', 'Rsd1231', 'Rsd1231']
"""одинаково слева направоstrlist = ['121', '123321']"""

strlist = list(filter(lambda x : x == x[::-1], strlist))

strlist = ['a', '123321', 'fsd1231', 'ii', 'Rsd1231']
"""с любой гласной aeiouyAEIOUY"""
strlist = ['a', 'ii']
b = "aeiouyAEIOUY"
strlist = list(filter(lambda x: any(ch in b for ch in x), strlist))
