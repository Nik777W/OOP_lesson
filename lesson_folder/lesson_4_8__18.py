# Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс Formatter должен иметь один статический метод:
#
# format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и выводящий
# информацию о переданном объекте в формате, зависящем от его типа. Если переданный объект принадлежит какому-либо
# другому типу, должно быть возбуждено исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается

from functools import singledispatchmethod


class Formatter:

    @singledispatchmethod
    @staticmethod
    def format(arg):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @staticmethod
    @format.register
    def _(arg: int):
        print('Целое число: ', end='')
        print(arg)

    @staticmethod
    @format.register
    def _(arg: float):
        print('Вещественное число: ', end='')
        print(arg)

    @staticmethod
    @format.register
    def _(arg: list):
        print('Элементы списка: ', end='')
        print(*arg, sep=', ')

    @staticmethod
    @format.register
    def _(arg: tuple):
        print('Элементы кортежа: ', end='')
        print(*arg)


    @staticmethod
    @format.register
    def _(arg: dict):
        print('Пары словаря: ', end='')
        print(*arg.items())

# TEST__1

Formatter.format(1337)
Formatter.format(20.77)

# TEST__2

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})

# TEST__3

Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
