from gettext import textdomain
from random import sample, choice
from re import match
from string import *
from re import *
import re

from PIL.ImagePalette import random

print(ascii_letters)
print(ascii_lowercase)
print(ascii_uppercase)
print(digits)
print(hexdigits)
print(octdigits)

print(whitespace)
print("".join('12123123123'))

str = 'ffrfijin2342311&^$%$%#$@'
str = 'f'
print(punctuation)
"""проще - используем join, генератор"""
#str = ''.join([char for char in str if])

str = '453876'
print(str[:3:])
print(str[3::])
"""написать функцию, возвращающую true 
если 1+2+3 == 4+5+6
или false в остальных """

print(ascii_letters)
print(digits)
print(hexdigits)
print(octdigits)

print(ascii_uppercase)
print(punctuation)
print(ascii_lowercase)

"""создать случайный логин и пароль
логин - заглавная буква + 10 строчных
пароль - заглавная, символ, 10 строчных"""



from random import *
login = choice(ascii_uppercase)
login += ''.join(choices(ascii_lowercase, k=10))
password = choice(ascii_uppercase)
password += ''.join(choice(punctuation))
password += ''.join(choices(ascii_lowercase, k=10))
print(login)
print(password)


pattern = r'.' # один любой символ
print(bool(match(pattern, '..')))

pattern = r'^qwe' # начало строки
print(bool(match(pattern, 'qwe')))

pattern = r'qwe$' # конец строки
print(bool(match(pattern, 'qwe')))

pattern = r'\.*' # любые символы, много
print(bool(match(pattern, '.2334')))

pattern = r'ab+8' # любое количество определенных символов
print(bool(match(pattern, 'ab888')))

pattern = r'ab?8$' # один конкретный символ
print(bool(match(pattern, 'ab8')))

pattern = r'ab{5}' # заданное количество повторений до {
print(bool(match(pattern, 'abbbbb')))

pattern = r'[123]$' # вхождение любого одного из [внутри]
print(bool(match(pattern, '2')))

pattern = r'[^b]$' # кроме вхождение любого одного из [внутри]
print(bool(match(pattern, 'a')))

pattern = r'(12|32)(12|45)' # или
print(bool(match(pattern, '1232')))

pattern = r'\d' # число
print(bool(match(pattern, '1')))

pattern = r'\d{11}' # 11 цифр
print(bool(match(pattern, '81231231212')))

pattern = r'\d{11, }' # 11 цифр и более
print(bool(match(pattern, '81231231212')))

pattern = r'\d{11, 15}' # от 11 до 15
print(bool(match(pattern, '81231231212')))

pattern = r'\D' # не число
print(bool(match(pattern, '1')))

pattern = r'\w' # буква цифра подчеркивание
print(bool(match(pattern, '1')))

pattern = r'\W' # кроме буква цифра подчеркивание
print(bool(match(pattern, '1')))

pattern = r'\s' # whitespace
print(bool(match(pattern, '1')))

pattern = r'\S' # не whitespace
print(bool(match(pattern, '1')))

pattern = r'.*\bqwe\b.*' # граница слова
print(bool(match(pattern, '1 qwe 123')))

pattern = r'^.\Brty\B.$' # внутри слова
print(bool(match(pattern, 'qrtyq')))



pattern = r'\d{}' # 11 цифр
print(bool(match(pattern, str)))

str = 'qweqw@tu.riu'

str = '+7(123)123-23-23'

pattern = r'^\w+[\.\w-]*@\w+[\.\w-]*\.\w+[\.\w-]*$' # 11 цифр
print(bool(match(r'^\w+[.\w-]*@\w+[.\w-]*\.\w+[.\w-]*$', 'e....6...------@')))


match1 = search(r'\d+', '123qwe333')
print(match1.group())

matches = findall(r'\d+', '123qwe333')
print(int(matches))

matches = finditer(r'\d+', '123qwe333')
for i in matches:
    print(i.group())

result = split(r'\s+', '123qwe333\tqweqwqw  qwe')
print(result)

result = sub('\d+','', '123qwe333\tqweqwqw  qwe')
print(type(result).__name__) #str

result = subn('\d+','', '123qwe333\tqweqwqw  qwe')
print(type(result).__name__) #tuple

pattern = compile('\d+')

match = search(pattern, 'gvugvugv123')
print(match.group())

class Cat():
    def __init__(self, color='black', age=0):
        self.color = color
        self.age = age

    def meow(self):
        print('meow')





cat = Cat()
cat.meow()