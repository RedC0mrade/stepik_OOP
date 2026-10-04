class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.__perimeter = 2 * (self.length + self.width)
        self.__area = self.length + self.width