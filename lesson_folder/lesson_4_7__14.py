# Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:
#
# name — имя домашнего животного
# Экземпляр класса Pet должен иметь один атрибут:
#
# name — имя домашнего животного
# Класс Pet должен иметь три метода класса:
#
# first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet. Если ни одного экземпляра еще не
# было создано, метод должен вернуть значение None
# last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet. Если ни одного экземпляра еще не
# было создано, метод должен вернуть значение None
# num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet


class Pet:
    first = None
    last = None
    total = 0

    def __init__(self, name):
        if self.__class__.first == None:
            self.__class__.first = self
        self.name = name
        self.__class__.last = self
        self.__class__.total += 1

    @classmethod
    def first_pet(cls):
        return cls.first

    @classmethod
    def last_pet(cls):
        return cls.last

    @classmethod
    def num_of_pets(cls):
        return cls.total


# TEST

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())