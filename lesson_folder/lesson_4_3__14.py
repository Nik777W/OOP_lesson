# Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.
# Экземпляр класса Postman должен иметь один атрибут:
# delivery_data — изначально пустой список адресов, по которым следует доставить письма
# Экземпляр класса Postman должен иметь три метода экземпляра:
# add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов
# эти данные в виде кортежа: (<улица>, <дом>, <квартира>)
# get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой
# улице, в которые требуется доставить письма
# get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в
# этом доме, в которые требуется доставить письма

class Postman:

    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, dep):
        self.delivery_data.append((street, house, dep))

    def get_houses_for_street(self, street):
        result = filter(lambda x: x[0] == street, self.delivery_data)
        return list(dict.fromkeys(map(lambda x: x[1], result)))

    def get_flats_for_house(self, street, house):
        result = filter(lambda x: x[0] == street and x[1] == house, self.delivery_data)
        return list(dict.fromkeys(map(lambda x: x[2], result)))


# TEST


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))