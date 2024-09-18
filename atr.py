class Cat():
    def __init__(self, breed, color, age):
        self._breed = breed
        self._color = color
        self._age = age

    @property
    def breed(self):
        return self._breed

    @property
    def color(self):
        return self._color

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age > self._age:
            self._age = new_age
        return self._age


cat = Cat('Абиссинская', 'Рыжая', 4)
print(cat.breed) # Абиссинская
print(cat.color) # Рыжая
print(cat.age) # 4
cat.age = 5
print(cat.age) # 5
cat.breed = 'Сиамская'
print(cat.breed) # AttributeError: can't set attribute on line 34 in cat.py
