# Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать
# один аргумент:
# birth_date — дата рождения, представленная в одном из следующих вариантов:
# экземпляр класса date
# строка с датой в ISO формате
# список или кортеж из трех целых чисел: года, месяца и дня
# Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено
# исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается
# Экземпляр класса BirthInfo должен иметь один атрибут:
# birth_date — дата рождения в виде экземпляра класса date
# Класс BirthInfo должен иметь одно свойство:
# age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет,
# прошедших с даты рождения на сегодняшний день
# Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения
# его возраст увеличивается на один год.

from functools import singledispatchmethod
from datetime import date

class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register
    def _(self, arg: date):
        self.birth_date = arg

    @__init__.register
    def _(self, arg: str):
        try:
            self.birth_date = date.fromisoformat(arg)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')


    @__init__.register(tuple | list)
    def _(self, arg):
        try:
            self.birth_date = date(*arg)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        a = date(1,1,1) + (date.today() - self.birth_date)
        return a.year - 1


# TEST__1

birthinfo1 = BirthInfo('2020-09-18')
birthinfo2 = BirthInfo(date(2010, 10, 10))
birthinfo3 = BirthInfo([2016, 1, 1])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)


# TEST__2

birthday = date(2020, 9, 18)
today = date.today()
birthinfo = BirthInfo(birthday)
print(birthinfo.age)

# TEST__3

birth_dates = ['2020-09-41', '2020-0918', '202009-18', ' 2020-09-18 ', '2020-9-18', '2020-41-09']

for birth_date in birth_dates:
    try:
        birthinfo1 = BirthInfo(birth_date)
    except TypeError as e:
        print(e)

# TEST__4

birth_dates = [
    [2020],
    (2020,),
    [2020, 1],
    [2020, 1, '1'],
    (2020, 1),
    (2020, 1, '1'),
    [2020, 1, 1, 1],
    (2020, 1, 1, 1),
    [2020, '1', '1'],
    [2020, '1', 1],
]

for birth_date in birth_dates:
    try:
        birthinfo = BirthInfo(birth_date)
    except TypeError as e:
        print(e)
