# Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:
# iterable — итерируемый объект
# Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable
# в исходном порядке, а затем возбуждает исключение StopIteration.
# Класс LoopTracker должен иметь четыре свойства:
# accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором на
# данный момент
# empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент
# опустевшего итератора
# first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его. Если
# итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено
# исключение AttributeError с текстом:
# Исходный итерируемый объект пуст
# last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный
# момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError
# с текстом:
# Последнего элемента нет
# Класс LoopTracker должен иметь один метод экземпляра:
# is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае


class LoopTracker:
    def __init__(self, iterable):
        self.count = 0
        self.error_count = 0
        self._first = None
        self.iterable = iter(iterable)
        self.res = next(self.iterable, 'empty')
        self._first = self.res
        self.temp = self.res

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.temp == self._first:
                self.temp = None
                self.count += 1
                return self.res
            else:
                self.res = next(self.iterable)
        except:
            self.error_count += 1
            raise StopIteration
        self.count += 1
        return self.res

    def is_empty(self):
        try:
            a = self.__next__()
            self.temp = self._first
            return False
        except StopIteration:
            return True

    @property
    def accesses(self):
        return self.count

    @property
    def empty_accesses(self):
        return self.error_count

    @property
    def first(self):
        if self.res == 'empty':
            raise AttributeError('Исходный итерируемый объект пуст')
        if self._first is None:
            self._first = self.__next__()
        return self._first

    @property
    def last(self):
        if self.res == self.temp:
            raise AttributeError('Последнего элемента нет')
        return self.res