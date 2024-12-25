# Реализуйте класс Numbers, описывающий изначально пустой расширяемый набор целых чисел. При создании
# экземпляра класс не должен принимать никаких аргументов.
# Класс Numbers должен иметь три метода экземпляра:
# add_number() — метод, принимающий в качестве аргумента целое число и добавляющий его в набор
# get_even() — метод, возвращающий список всех четных чисел из набора
# get_odd() — метод, возвращающий список всех нечетных чисел из набора

class Numbers:

    def __init__(self):
        self.numeros = []

    def add_number(self, n):
        self.numeros.append(n)

    def get_even(self):
        return list(i for i in self.numeros if i % 2 == 0)

    def get_odd(self):
        return list(i for i in self.numeros if i % 2 == 1)

# TEST

numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())
