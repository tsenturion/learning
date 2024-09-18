"""https://github.com/tsenturion/learning"""

from re import *

try:
    with open('pupils.txt', 'r', encoding='utf-8') as file:
        for line in file:
            """print(line.split())
            print(line[len(line) - 2])
            for i in line:
                if i.isdigit():
                    print(i)"""
            matches = search(r'\d', line)
            print(int(matches.group()))
except FileNotFoundError as ex:
    print(ex)
    print(FileNotFoundError)
except IOError as ex:
    print(ex)
    print(IOError)

"""посчитать средний балл
посчитать количество отличников (в одну строчку)
записать результат в файл results.txt
"""
with open('results.txt', 'w', encoding='utf-8') as file:
    file.write('ваши результаты')
