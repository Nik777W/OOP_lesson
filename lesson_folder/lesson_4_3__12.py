# Будем называть словом любую последовательность из одной или более букв. Текстом будем считать набор слов,
# разделенных пробельными символами.
# Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра
# класс не должен принимать никаких аргументов.
# Экземпляр класса TextHandler должен иметь три метода:
# add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
# get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
# get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе


class TextHandler:

    def __init__(self):
        self.list_text = []

    def add_words(self, text):
        self.list_text.extend(text.split())

    def get_shortest_words(self):
        min_len_list = []
        if self.list_text:
            min_len_list = list(filter(lambda x: len(x) == len(min(self.list_text, key=len)), self.list_text))
        return min_len_list

    def get_longest_words(self):
        max_len_list = []
        if self.list_text:
            max_len_list = list(filter(lambda x: len(x) == len(max(self.list_text, key=len)), self.list_text))
        return max_len_list

# TEST

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())