class Rectangle:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._perimeter = 2 * (self._length + self._width)
        self._area = self._length * self._width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length
        self._perimeter = 2 * (self._length + self._width)
        self._area = self._length * self._width

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        self._perimeter = 2 * (self._length + self._width)
        self._area = self._length * self._width

    def get_perimeter(self):
            return self._perimeter

    def get_area(self):
            return self._area
        
    length = property(get_length, set_length)
    width = property(get_width, set_width)
    perimeter = property(get_perimeter)
    area = property(get_area)

# INPUT DATA:

# TEST_1:

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

# # TEST_3:
# rectangle = Rectangle(20, 20)
# array = [(39, 48), (64, 36), (80, 56), (79, 60), (47, 30), (26, 27), (47, 69), (77, 22), (28, 78), (33, 75)]
# for length, width in array:
#     rectangle.length = length
#     rectangle.width = width
#     print(f'Периметр = {rectangle.perimeter}, Площадь = {rectangle.area}')
