#!/usr/bin/python3
'''
My module
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle Class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''
        area calculates area of rectangle
        '''
        return self.__height * self.__width

    def display(self):
        '''
        display prints rectangle on output
        '''
        if self.height == 0 or self.width == 0:
            print()
        else:
            for i in range(self.y):
                print()
            for j in range(self.height):
                print(" " * self.x + "#" * self.width)

    def __str__(self):
        c_n = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}".format(
            c_n, self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        '''
        update updates attributes of instance
        '''
        arglist = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, arglist[i], args[i])
        else:
            for k in kwargs.keys():
                setattr(self, k, kwargs[k])

    def to_dictionary(self):
        '''
        to_dictionary returns dictionary of the object
        '''
        new_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }
        return new_dict
