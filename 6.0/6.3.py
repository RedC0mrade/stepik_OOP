class Person:

    def __init__(self, name: str, surname: str):

        self.name = name
        self.surname = surname

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_surname(self):
        return self._surname

    def set_surname(self, surname):
        self._surname = surname
    
    def get_fullname(self):
        return self._name + ' ' + self._surname

    def set_fullname(self, fullname: str):
        self._name, self._surname = fullname.split()


    name = property(get_name, set_name)
    surname = property(get_surname, set_surname)
    fullname = property(get_fullname, set_fullname)


# INPUT DATA:

# TEST_1:
person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)

# TEST_2:
person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)

# TEST_3:
person = Person('Алан', 'Тьюринг')

person.surname = 'Вирт'
print(person.fullname)

# TEST_4:
person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)

# TEST_5:
person = Person('Брайан', 'Керниган')
print(hasattr(person, 'name'))
print(hasattr(person, 'surname'))
print(hasattr(person, 'fullname'))