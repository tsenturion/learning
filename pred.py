class Predator:
    def hunt(self):
        print('Охотится...')


class Cat(Predator):
    def __init__(self, name, color):
        super().__init__()
        self._name = name
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color


cat = Cat('Даниэла', 'Чёрный')
cat.hunt()  # Охотится…
