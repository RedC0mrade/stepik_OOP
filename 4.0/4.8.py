class Bee:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
    ):
        self.x = x
        self.y = y

    def move_up(self, n: int):
        self.y += n


    def move_down(self, n: int):
        self.y -= n


    def move_right(self, n: int):
        self.x += n


    def move_left(self, n: int):
        self.x -= n


bee = Bee()

print(bee.x, bee.y)

bee = Bee()

bee.move_up(1)
bee.move_right(1)
bee.move_down(1)
bee.move_left(1)

print(bee.x, bee.y)



bee = Bee()

bee.move_right(2)
bee.move_right(2)
bee.move_up(3)
bee.move_left(1)
bee.move_down(1)

print(bee.x, bee.y)