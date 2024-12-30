# Реализуйте класс HourClock, описывающий часы с одной лишь часовой стрелкой. При создании экземпляра класс должен
# принимать один аргумент:
# hours — количество часов. Если hours не является целым числом, принадлежащим диапазону [1; 12], должно быть
# возбуждено исключение ValueError с текстом:
# Некорректное время
# Класс HourClock должен иметь одно свойство:
# hours — свойство, доступное для чтения и записи, возвращающее текущее количество часов. При изменении свойство
# должно проверять, что новое значение является целым числом, принадлежащим диапазону [1; 12], в противном случае
# должно быть возбуждено исключение ValueError с текстом:
# Некорректное время
# Примечание 1. Никаких ограничений касательно реализации класса HourClock нет, она может быть произвольной.

class HourClock:

    def __init__(self, hours):
        self.hours = hours

    def get_hours(self):
        return self._hours

    def set_hours(self, n):
        if isinstance(n, int) and n in range(1, 13):
            self._hours = n
        else:
            raise ValueError('Некорректное время')

    hours = property(get_hours, set_hours)



# TEST

time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)

# TEST__2

try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)
