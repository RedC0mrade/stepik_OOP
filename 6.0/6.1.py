class Rectangle:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.perimeter = 2 * (self._length + self._width)
        self.area = self._length * self._width

        def get_length(self):
            return self._length

        def set_length(self, length):
            print(1)
            self._length = length
            self.perimeter = 2 * (self._length + self._width)
            self.area = self._length + self._width

        def get_width(self):
            return self._width

        def set_width(self, width):
            print(2)
            self._width = width
            self.perimeter = 2 * (self._length + self._width)
            self.area = self._length + self._width
        
        
        length = property(get_length, set_length)
        width = property(get_width, set_width)


# # INPUT DATA:

# # TEST_1:
# rectangle = Rectangle(4, 5)

# print(rectangle.length)
# print(rectangle.width)
# print(rectangle.perimeter)
# print(rectangle.area)

# # TEST_2:
# rectangle = Rectangle(4, 5)

# rectangle.length = 2
# rectangle.width = 3
# print(rectangle.length)
# print(rectangle.width)
# print(rectangle.perimeter)
# print(rectangle.area)

# TEST_3:
rectangle = Rectangle(20, 20)
array = [(39, 48), (64, 36), (80, 56), (79, 60), (47, 30), (26, 27), (47, 69), (77, 22), (28, 78), (33, 75)]
for length, width in array:
    rectangle.length = length
    rectangle.width = width
    print(f'Периметр = {rectangle.perimeter}, Площадь = {rectangle.area}')
