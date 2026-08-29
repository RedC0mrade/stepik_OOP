class User:

    def __init__(self, name: str, friends:int = 0):

        self.name = name
        self.friends = friends

    def add_friends(self, n: int):
        self.friends += n