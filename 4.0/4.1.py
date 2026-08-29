class Cat:
    pass


cat = Cat()

cat.breed = 'Британский'
cat.name = 'Кемаль'
cat.age = 1

print(cat.breed, cat.name)        # обращение к атрибутам

cat.age += 2                      # изменение значения атрибута
print(cat.age)