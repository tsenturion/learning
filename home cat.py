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

    def purr(self):
        print('Мрррр')


class HomeCat(Cat):
    def __init__(self, breed, color, age, owner, name):
        super().__init__(breed, color, age)
        self._owner = owner
        self._name = name

    @property
    def owner(self):
        return self._owner

    @property
    def name(self):
        return self._name

    def getTreat(self):
        print('Мяу-мяу')


my_cat = HomeCat('Сиамская', 'Белая', 3, 'Иван', 'Роза')

print(my_cat.owner)
print(my_cat.breed)
my_cat.getTreat() # Мяу-мяу
my_cat.purr() # Мрррр
