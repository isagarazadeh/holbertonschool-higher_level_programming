#!/usr/bin/python3
'''Square with private size attribute and check'''


class Square:
    '''Gets size as its attribute'''
    def __init__(self, size=0):
        '''
        Init block of Square Class
        '''
        self.size = size

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

    def my_print(self):
        '''
        my_print prints a square
        '''
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
