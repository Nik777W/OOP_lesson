# Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего
# подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы.
# Например, bee_geek и hello_world.
# Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без
# пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.
# Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case
# и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.
# Класс CaseHelper должен иметь четыре статических метода:
# is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана
# в стиле Snake Case, или False в противном случае
# is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка
# записана в стиле Upper Camel Case, или False в противном случае
# to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в
# стиле Snake Case и возвращает полученный результат
# to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в
# стиле Upper Camel Case и возвращает полученный результат

from re import fullmatch
class CaseHelper:
    @staticmethod
    def is_snake(my_string):
        return True if fullmatch(r'^[^_A-Z][a-z_]+$', my_string) else False
    @staticmethod
    def is_upper_camel(my_string):
        return True if fullmatch(r'^([A-Z][a-z]+)+$', my_string) else False

    @staticmethod
    def to_snake(my_string):
        return ''.join([f'_{i.lower()}' if i.upper() == i and n != 0 else i.lower() for n, i in enumerate(my_string)])

    @staticmethod
    def to_upper_camel(my_string: str):
        my_string = my_string.replace('_', ' ').title().replace(' ','')
        return my_string



# TEST__1

print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))

# TEST__2
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))

# TEST__3

cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex', 'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))