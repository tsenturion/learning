"""https://github.com/tsenturion/learning"""

try:
    with open('pupils.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
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