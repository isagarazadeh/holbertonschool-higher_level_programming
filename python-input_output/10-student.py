#!/usr/bin/python3
'''
10-student.py
'''


class Student:
    '''
    Student class
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        diction = {}
        if attrs is None:
            diction = self.__dict__
        else:
            for i in self.__dict__.keys():
                if i in attrs:
                    diction[i] = self.__dict__[i]
        return diction
