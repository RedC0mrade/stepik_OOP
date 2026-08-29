class User:

    def __init__(self, name: str, friends:int = 0):

        self.name = name
        self.friends = friends

    def add_friends(self, n: int):
        self.friends += n


user = User('Arthur')

print(user.friends)


user = User('Timur')

user.add_friends(2)
user.add_friends(2)
user.add_friends(3)

print(user.friends)