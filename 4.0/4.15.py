class Todo:
    def __init__(self):
        self.things = list()
        self.up = float('-inf')
        self.down = float('inf')

    def add(self, name: str, priority: int):
        self.things.append((name, priority))
        self.up = max(self.up, priority)
        self.down = min(self.down, priority)

    def get_by_priority(self, n: int):
        return [x[0] for x in self.things if x[1] == n]
        

    def get_low_priority(self):
        return self.get_by_priority(self.down)

    def get_high_priority(self):
        return self.get_by_priority(self.up)



todo = Todo()

print(todo.things)
print(todo.get_by_priority(1))
print(todo.get_low_priority())
print(todo.get_high_priority())



# todo = Todo()

# todo.add('Проснуться', 3)
# todo.add('Помыться', 2)
# todo.add('Поесть', 2)

# print(todo.get_by_priority(2))



todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))

todo = Todo()

todos = [
    'Выбрать хостинг для своего сайта',
    'Записаться к стоматологу',
    'Записаться на курсы английского',
    'Навести порядок на кухне',
    'Подготовить одежду к лету',
    'Подготовиться к выступлению в понедельник',
    'Помыть машину',
    'Пропылесосить ковры',
    'Свозить Кемаля к ветеринару',
    'Сходить в парикмахерскую',
    'Посетить выставку камней'
]

priorities = [4, 1, 2, 5, 2, 5, 5, 3, 3, 3, 4]
for t, p in zip(todos, priorities):
    todo.add(t, p)

print(todo.things)
print(todo.get_by_priority(3))
print(todo.get_low_priority())
print(todo.get_high_priority())