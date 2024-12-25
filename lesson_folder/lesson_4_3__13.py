# Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
# Экземпляр класса Todo должен иметь один атрибут:
# things — изначально пустой список дел, которые нужно выполнить
# Класс Todo должен иметь четыре метода экземпляра:
# add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в
# виде кортежа:(<название дела>, <приоритет>)
# get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел,
# имеющих приоритет n
# get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
# get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет


class Todo:

    def __init__(self):
        self.things = []

    def add(self, name, num):
        case= (name, num)
        self.things.append(case)

    def get_by_priority(self, n):
        return [i[0] for i in self.things if i[1] == n]

    def get_low_priority(self):
        return [i[0] for i in self.things if i[1] == min([i[1] for i in self.things])]

    def get_high_priority(self):
        return [i[0] for i in self.things if i[1] == max([i[1] for i in self.things])]

# TEST

todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))