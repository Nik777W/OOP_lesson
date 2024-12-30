# Реализуйте класс Matrix, описывающий двумерную матрицу. При создании экземпляра класс должен принимать
# три аргумента в следующем порядке:
# rows — количество строк в матрице
# cols — количество столбцов в матрице
# value — начальное значение для элементов матрицы, по умолчанию имеет значение 0
# Экземпляр класса Matrix должен иметь два атрибута:
# rows — количество строк в матрице
# cols — количество столбцов в матрице
# Класс Matrix должен иметь два метода экземпляра:
# get_value() — метод, принимающий в качестве аргументов строку row и столбец col и возвращающий элемент матрицы
# со строкой row и столбцом col
# set_value() — метод, принимающий в качестве аргументов строку row, столбец col и значение value и устанавливающий
# в качестве значения элемента матрицы со строкой row и столбцом col значение value
# Экземпляр класса Matrix должен иметь следующее формальное строковое представление:
# Matrix(<количество строк в матрице>, <количество столбцов в матрице>)
# Неформальным строковым представлением должна быть строка, в которой перечислены все элементы матрицы. Элементы
# строки матрицы должны быть разделены пробелом, строки матрицы должны быть разделены символом переноса строки \n.
# Например, для объекта Matrix(2, 3) неформальным строковым представлением должна быть строка 0 0 0\n0 0 0,
# которая при выводе будет отображаться следующим образом:
#
# 0 0 0
# 0 0 0
# Также экземпляр класса Matrix должен поддерживать унарные операторы +, - и ~:
# результатом унарного + должен являться новый экземпляр класса Matrix c исходным количеством строк и
# столбцов и с исходными элементами
# результатом унарного - должен являться новый экземпляр класса Matrix c исходным количеством строк и
# столбцов и с элементами, взятыми с противоположным знаком
# результатом унарного ~ должен являться новый экземпляр класса Matrix, представляющий транспонированную матрицу
# Наконец, при передаче экземпляра класса Matrix в функцию round() должен возвращаться новый экземпляр класса Matrix
# c исходным количеством строк и столбцов и с элементами, округленными с помощью функции round(). Во время передачи в
# функцию round() должна быть возможность в качестве второго необязательного аргумента указать целое число,
# определяющее количество знаков после запятой при округлении.


class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[str(value) for _ in range(cols)] for _ in range(rows)]

    def get_value(self, x, y):
        return self.matrix[x][y]

    def set_value(self, rows, cols, value):
        self.matrix[rows][cols] = str(value)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.rows}, {self.cols})'

    def __str__(self):
        a = '\n'.join(' '.join(i) for i in self.matrix)
        return a

    def __pos__(self):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.matrix = self.matrix
        return new_matrix
    def __neg__(self):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.matrix = [[j[1:] if j[0] == '-' else f'-{j}' for j in i] for i in self.matrix]
        return new_matrix

    def __invert__(self):
        new_matrix = Matrix(self.cols, self.rows)
        new_matrix.matrix = list(zip(*self.matrix))
        return new_matrix

    def __round__(self, n=0):
        new_matrix = Matrix(self.rows, self.cols)
        new_matrix.matrix = [[str(round(float(j),n)) for j in i] for i in self.matrix]
        return new_matrix

# TEST__1


matrix = Matrix(5, 10)

floats = [[7125.900408, 633.354471, -9237.8575119, 2865.3825158, 5509.2609336, 8712.260779, 8317.523947, 2512.4736075,
           -3087.5496014, 3861.68814],
          [-7852.451832, 376.465911, -8142.7867326, -6921.8371407, 3735.7516227, -3322.8019034, 7115.79968,
           -8949.9313078, -7032.4347679, -5217.8236385],
          [-7817.9657992, -4319.716346, -1038.6294521, -2959.8970273, -9263.5713405, 9358.607686, 1429.6576196,
           -9484.68116, 639.6343972, 3444.9938213],
          [-2844.2405153, -2078.2441427, 6812.1367017, 112.3910618, -1116.8662449, 5042.7026276, -5981.6930342,
           4370.9173164, -8851.7648474, 8990.6896422],
          [90.8102435, 5256.6137481, -9743.8477321, -131.5501688, -5920.5976176, 4963.8336619, -4907.3622526,
           8531.2015615, -244.3630074, 3421.8817151]]

for r in range(5):
    for c in range(10):
        matrix.set_value(r, c, floats[r][c])

print(matrix)
print()
print(~matrix)
print()
print(round(matrix, 2))
print()
print(-matrix)

# TEST__2

matrix = Matrix(2, 3, 1)

print(+matrix)
print()
print(-matrix)

# TEST__3

matrix = Matrix(2, 3, 1)

plus_matrix = +matrix
minus_matrix = -matrix
invert_matrix = ~matrix

print(plus_matrix.cols, plus_matrix.rows)
print(minus_matrix.cols, minus_matrix.rows)
print(invert_matrix.cols, invert_matrix.rows)