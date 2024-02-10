#!/usr/bin/python3
'''
This module has a class named Rectangle
'''


class Rectangle:
    '''
    An object rectangle is defined
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        # Returns rectangle using # signs
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
