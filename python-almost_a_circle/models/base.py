#!/usr/bin/python3
'''
My module
'''
import json
import turtle


class Base:
    '''
    Base Class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        save_to_file writes the JSON string of list_objs to a file
        Args:
            list_objs: object list
        '''
        c_n = cls.__name__
        if list_objs is None:
            with open("{}.json".format(c_n), "w", encoding="utf-8") as f:
                f.write("[]")
        else:
            li = []
            for i in list_objs:
                li.append(i.to_dictionary())
            with open("{}.json".format(c_n), "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 2)
        else:
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        c_n = cls.__name__
        li_obj = []
        li = []
        try:
            with open("{}.json".format(c_n), "r", encoding="utf-8") as f:
                li = cls.from_json_string(f.read())
        except IOError:
            return []
        for i in li:
            li_obj.append(cls.create(**i))
        return li_obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.title("Drawing")

        def rectangle(x, y, width, height):
            t.penup()
            t.goto(x, y)
            t.pendown()
            for i in range(2):
                t.forward(width)
                t.right(90)
                t.forward(height)
                t.right(90)

        def square(x, y, side_length):
            t.penup()
            t.goto(x, y)
            t.pendown()
            for i in range(4):
                t.forward(side_length)
                t.right(90)

        for rectangle in list_rectangles:
            rectangle(
                rectangle.x,
                rectangle.y,
                rectangle.width,
                rectangle.height,
            )

        for square in list_squares:
            square(square.x, square.y, square.size)

        screen.exitonclick()
