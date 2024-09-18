class Cat:
    def sleep(self):
        print('Свернулся в клубок и сладко спит.')


class Parrot:
    def sleep(self):
        print('Сел на жёрдочку и уснул.')


def homeSleep(animal):
    animal.sleep()


cat = Cat()
parrot = Parrot()
homeSleep(cat)  # Свернулся в клубок и сладко спит.
homeSleep(parrot)  # Сел на жёрдочку и уснул.
