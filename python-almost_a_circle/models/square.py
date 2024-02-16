#!/usr/bin/python3
'''
module

'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square Class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        c_n = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}".format(c_n, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        update updates attributes of instance
        '''
        arglist = ["id", "size", "x", "y"]
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
                "size": self.size,
                "x": self.x,
                "y": self.y
        }
        return new_dict
