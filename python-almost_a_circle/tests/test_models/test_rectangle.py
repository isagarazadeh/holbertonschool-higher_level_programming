#!/usr/bin/python3
'''
Tests for rectangle model
'''
import os
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.area(), 2)

    def test_str(self):
        r0 = Rectangle(1, 2, id=66)
        self.assertEqual(str(r0), "[Rectangle] (66) 0/0 - 1/2")

    def test_display1(self):
        r0 = Rectangle(2, 5)
        expected_output = "##\n##\n##\n##\n##\n"
        with patch("sys.stdout", new=StringIO()) as f:
            r0.display()
            self.assertEqual(f.getvalue(), expected_output)

    def test_display_2(self):
        r0 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as f:
            r0.display()
            self.assertEqual(f.getvalue(), expected_output)

        r0.width = 5
        expected_output = "#####\n#####\n"
        with patch("sys.stdout", new=StringIO()) as f:
            r0.display()
            self.assertEqual(f.getvalue(), expected_output)

    def test_display_3(self):
        r0 = Rectangle(5, 4, 1, 1)
        expected_output = "\n #####\n #####\n #####\n #####\n"
        with patch("sys.stdout", new=StringIO()) as f:
            r0.display()
            self.assertEqual(f.getvalue(), expected_output)

    def test_display_4(self):
        r0 = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch("sys.stdout", new=StringIO()) as f:
            r0.display()
            self.assertEqual(f.getvalue(), expected_output)

        r0.x = 4
        expected_output = "    ###\n    ###\n"
        with patch("sys.stdout", new=StringIO()) as f:
            r0.display()
            self.assertEqual(f.getvalue(), expected_output)

        r0.y = 2
        expected_output = "\n\n    ###\n    ###\n"
        with patch("sys.stdout", new=StringIO()) as f:
            r0.display()
            self.assertEqual(f.getvalue(), expected_output)

    def test_to_dictionary(self):
        r0 = Rectangle(3, 2, id=55)
        self.assertEqual(
            r0.to_dictionary(), {"id": 55, "width": 3, "height": 2, "x": 0, "y": 0}
        )

    def test_update(self):
        r0 = Rectangle(10, 10, 10, 10)
        r0.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r0), "[Rectangle] (89) 4/5 - 2/3")

    def test_create(self):
        r0_dictionary = {"x": 3, "y": 4, "id": 89, "height": 2, "width": 1}
        r1 = Rectangle.create(**r0_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/4 - 1/2")

    def test_save_to_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([Rectangle(1, 2, id=13)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                f.read(), '[{"id": 13, "width": 1, "height": 2, "x": 0, "y": 0}]'
            )

    def test_load_from_file1(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_2(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

        r1 = Rectangle(5, 5)

        inp = [r1]
        Rectangle.save_to_file(inp)
        out = Rectangle.load_from_file()

        self.assertEqual(inp[0].__str__(), out[0].__str__())


if __name__ == "__main__":
    unittest.main()
