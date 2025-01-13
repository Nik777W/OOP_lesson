# Реализуйте класс RomanNumeral, описывающий число в римской системе счисления. При создании экземпляра класс должен
# принимать один аргумент:
# number — число в римской системе счисления. Например, IV
# Экземпляр класса RomanNumeral должен иметь следующее неформальное строковое представление:
# <число в римской системе счисления>
# Помимо этого, экземпляр класса RomanNumeral должен поддерживать приведение к типу int, при приведении к которому
# его значением должно являться целое число в десятичной системе счисления, которому он соответствует.
# Также экземпляры класса RomanNumeral должны поддерживать между собой все операции сравнения с помощью
# операторов ==, !=, >, <, >=, <=.
# Наконец, экземпляры класса RomanNumeral должны поддерживать между собой операции сложения и вычитания с помощью
# операторов + и - соответственно:
# результатом сложения должен являться новый экземпляр класса RomanNumeral, представляющий сумму исходных
# результатом вычитания должен являться новый экземпляр класса RomanNumeral, представляющий разность исходных
# Примечание 1. Гарантируется, что из римского числа всегда вычитается строго меньшее римское число.
# Примечание 2. Подробнее про римскую систему счисления можно почитать по ссылке.
# Примечание 3. Не забывайте, что именно константу NotImplemented рекомендуется возвращать в методах, реализующих
# арифметические операции или операции сравнения, если эти операции для объектов каких-либо типов не определены.

from functools import total_ordering


@total_ordering
class RomanNumeral:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def __int__(self):
        NUM = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = [NUM[i] for i in self.number]+[0]
        tot = []
        for i in range(len(num)-1):
            if num[i] >= num[i+1]:
                tot.append(num[i])
            else:
                tot.append(-num[i])
        return sum(tot)

    @staticmethod
    def from_rom(n):
        tot = ''
        NUM = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
               100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
               10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
               }
        for k,v in NUM.items():
            while n >=k:
                n -= k
                tot += v
        return tot

    def __add__(self, other):
        return RomanNumeral(RomanNumeral.from_rom((self.__int__()) + (other.__int__())))

    def __sub__(self, other):
        return RomanNumeral(RomanNumeral.from_rom((self.__int__()) - (other.__int__())))

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.from_rom(self.__int__()) == RomanNumeral.from_rom(other.__int__())
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.from_rom(self.__int__()) < RomanNumeral.from_rom(other.__int__())
        return NotImplemented


# TEST_1:
number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))

# TEST_2:
number = RomanNumeral('X') - RomanNumeral('VI')

print(number)
print(int(number))

# TEST_3:
a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_4:
a = RomanNumeral('X')
b = RomanNumeral('X')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_5:
number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')

print(number)
print(int(number))

# TEST_6:
number = RomanNumeral('I') + RomanNumeral('II') + RomanNumeral('III') - RomanNumeral('V')

print(number)
print(int(number))

# TEST_7:
romans1 = ['I', 'X', 'L', 'IV', 'IX', 'XLV', 'CXXIV', 'MCMXCIV']
romans2 = ['I', 'V', 'L', 'VI', 'XI', 'XXV', 'CDXLVIII', 'MCMXCI']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))

# TEST_8:
romans1 = ['III', 'X', 'L', 'C', 'M', 'XXV', 'XC', 'MMMCMXXXV']
romans2 = ['II', 'V', 'X', 'L', 'D', 'IV', 'VIII', 'MCMXCIV']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))

# TEST_9:
romans = ['I', 'IV', 'IX', 'XII', 'XXV', 'XLV', 'LXIX', 'XC', 'CDXLVIII']

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))

# TEST_10:
roman = RomanNumeral('L')
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: 'one'}))