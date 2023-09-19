#!/usr/bin/python3
"""to serialise/deserialise"""
import json
import os
"""
This module contains the class base that
is used to instantiate the id
Author: Nafeesah
"""


class Base:
    """
    This is class named Base.

    Attributes:
        nb_objects(int): number of instances
        id(int): id of class instances

    Methods:
        None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """To instantiate object attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        objects_to_json = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(objects_to_json))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            string_data = []
        else:
            string_data = json.loads(json_string)
        return string_data

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if issubclass(cls, Base):
            if cls.__name__ == "Base":
                return Base(dictionary.get("id", None))

            if cls.__name__ == "Square":
                obj = cls(1)
            else:
                obj = cls(1, 1)

            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        output = []
        file_path = f"{cls.__name__}.json"
        if not os.path.exists(file_path):
            return output

        with open(f"{cls.__name__}.json", "r") as f:
            json_data = f.read()
            json_dic = cls.from_json_string(json_data)
            for i in json_dic:
                output.append(cls.create(**i))
        return output


class Rectangle(Base):
    """
    A class named rectangle

    Attributes:
        width(int): width of rectangle
        height(int): height of rectangle
        x(int):
        y(int):

    Methods:
        None
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """To initialize class instance attributes"""
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """To calculate area of rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """To display rectangle"""
        if self.__y > 0:
            for j in range(self.__y):
                print("")
        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        """Magic method to overwrite"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

    def to_dictionary(self):
        """To return dictionary containing attributes"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return (dic)


class Square(Rectangle):
    """
    A class named square inherited from Rectangle

    Attributes:
        size(int): length of one side of square
        x(int): the horizontal axis
        y(int): the vertical axis
        id(int): the id of the class instance

        Methods:
            None:
    """

    def __init__(self, size, x=0, y=0, id=None):
        """to initialize object instances"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Overloading"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """To update arguments"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To return dictionary containing attributes"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return (dic)
