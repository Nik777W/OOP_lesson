# Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента
# в следующем порядке:
# horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
# vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
# color — цвет коня (black или white)
# Экземпляр класса Knight должен иметь три атрибута:
# horizontal — координата коня на шахматной доске по горизонтальной оси
# vertical — координата коня на шахматной доске по вертикальной оси
# color — цвет коня
# Класс Knight должен иметь четыре метода экземпляра:
# get_char() — метод, возвращающий символ N
# can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и
# возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
# move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и
# заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с
# указанными координатами, его координаты должны остаться неизменными
# draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться
# конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь,
# — символом *

class Knight:

    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, hor, ver):
        temp_hor, hor  = ord(self.horizontal) - 97, ord(hor) - 97
        if abs(temp_hor - hor) * abs(self.vertical - ver) == 2:
            return True
        else:
            return False

    def move_to(self, hor, ver):
        temp_hor, hor_t = ord(self.horizontal) - 97, ord(hor) - 97
        if abs(temp_hor - hor_t) * abs(self.vertical - ver) == 2:
            self.horizontal = hor
            self.vertical = ver

    def draw_board(self):
        temp_hor = ord(self.horizontal) - 97
        tem_ver = 8 - self.vertical
        a = [['.']* 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if abs(temp_hor - i) * abs(tem_ver - j) == 2:
                    a[j][i] = '*'
        a[tem_ver][temp_hor] = 'N'
        [print(*i, sep='') for i in a]




# TEST

knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
knight.draw_board()
knight = Knight('c', 3, 'white')

knight.draw_board()
