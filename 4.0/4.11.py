class Scales:

    def __init__(self):
        self.right_scale = 0
        self.left_scale = 0

    def add_right(self, cargo: int):
        self.right_scale += cargo

    def add_left(self, cargo: int):
        self.left_scale += cargo

    def get_result(self):
        if self.left_scale == self.right_scale:
            return "Весы в равновесии"
        elif self.left_scale > self.right_scale:
            return "Левая чаша тяжелее"
        else:
            return "Правая чаша тяжелее"


scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

scales = Scales()

scales.add_right(1)
scales.add_left(2)

print(scales.get_result())

scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())