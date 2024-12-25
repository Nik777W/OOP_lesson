# Будем называть словом любую последовательность из одной или более латинских букв.
#
# Реализуйте класс Wordplay, описывающий расширяемый набор слов. При создании экземпляра класс должен принимать
# один аргумент:
# words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым
# Экземпляр класса Wordplay должен иметь один атрибут:
# words — список, содержащий набор слов
# Класс Wordplay должен иметь четыре метода экземпляра:
# add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор. Если слово уже есть в наборе,
# метод ничего не должен делать
# words_with_length() — метод, принимающий в качестве аргумента натуральное число n и возвращающий список слов из
# набора, длина которых равна n
# only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора, которые
# включают в себя только переданные буквы
# avoid() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из списка words,
# которые не содержат ни одну из этих букв
# Примечание 1. Слова в списках, возвращаемых методами words_with_length(), only() и avoid(), должны располагаться
# в том порядке, в котором они были добавлены.
# Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на основе которого он был создан. Другими
# словами, если исходный список изменится, то экземпляр класса Wordplay измениться не должен.


import copy


class Wordplay:

    def __init__(self, words=[]):
        self.words = copy.deepcopy(words)

    def add_word(self, world):
        if world not in self.words:
            self.words.append(world)

    def words_with_length(self, n):
        return [i for i in self.words if len(i) == n]

    def only(self, *args):
        total =[]
        for i in self.words:
            a = []
            for j in i:
                if j in args:
                    a.append(True)
                else:
                    a.append(False)
                    break
            if all(a):
                total.append(i)
        return total

    def avoid(self, *args):
        total = []
        for i in self.words:
            a = []
            for j in i:
                if j in args:
                    a.append(False)
                    break
                else:
                    a.append(True)
            if all(a):
                total.append(i)
        return total

# TEST

words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)

wordplay.add_word('python')
print(wordplay.words_with_length(4))
wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.avoid('a', 'b', 'c'))