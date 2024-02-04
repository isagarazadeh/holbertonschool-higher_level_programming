#!/usr/bin/python3
'''Square with private size attribute and check'''


class Square:
    '''Gets size and position as its attribute'''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Init block of Square Class
        '''
        self.size = size
        self.position = position

    def area(self):
        '''Calculates the area of square'''
        return self.__size ** 2

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        size setter

        Args:
            value: value of the size
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''
        position getter
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        position setter

        Args:
            value: value of position
        '''
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and value[0] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[1], int) and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        '''
        my_print prints a square
        '''
        if self.size == 0:
            print()
        else:
            for b in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
