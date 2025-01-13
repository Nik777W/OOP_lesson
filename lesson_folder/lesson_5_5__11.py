# Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:
# string — значение строки
# Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:
# <значение строки>
# Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью
# оператора +, результатом которой должен являться новый экземпляр класса SuperString, представляющий
# конкатенацию исходных.
# Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево и
# побитового сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:
# результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную строку,
# умноженную на n.
# результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из первых m
# символов исходной строки, где m — длина исходной строки, поделенная нацело на n
# результатом побитового сдвига влево должен являться новый экземпляр класса SuperString, представляющий
# исходную строку без последних n символов. Если n больше или равно длине исходной строки, результатом должен
# являться экземпляр класса SuperString, представляющий пустую строку
# результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString, представляющий
# исходную строку без первых n символов. Если n больше или равно длине исходной строки, результатом должен
# являться экземпляр класса SuperString, представляющий пустую строку
# Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность
# умножить как строку на число, так и число на строку.
# Примечание 1. Гарантируется, что экземпляр класса SuperString всегда делится на ненулевое число.
#

class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return self.__class__(self.string + other.string)
        return NotImplemented

    def __mul__(self, num):
        if isinstance(num, int):
            return self.__class__(self.string * num)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, num):
        if isinstance(num, int):
            n = len(self.string) // num
            return self.__class__(self.string[:n])
        return NotImplemented

    def __lshift__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        if n >= (temp_s := len(self.string)):
            return self.__class__('')
        return self.__class__(self.string[:temp_s - n])

    def __rshift__(self, n):
        if not isinstance(n, int):
            return NotImplemented
        if n >= len(self.string):
            return self.__class__('')
        return self.__class__(self.string[n:])

# TEST__1

s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)

# TEST__2

s1 = SuperString('bee')
s2 = SuperString('geek')