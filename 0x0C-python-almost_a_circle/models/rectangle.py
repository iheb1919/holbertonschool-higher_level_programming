#!/usr/bin/python3
"""class rectangle"""


from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class rectangle
        Attr:
           width(getter/setter)
           height(getter/setter)
           x(getter/setter)
           y(getter/setter)
       Class constructor:
           def __init__(self, width, height, x=0, y=0, id=None)

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area"""
        return self.__width * self.__height

    def display(self):
        """ display"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ __str___"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update """
        if args:
            if (len(args) > 0):
                self.id = args[0]
            if (len(args) > 1):
                self.__width = args[1]
            if (len(args) > 2):
                self.__height = args[2]
            if (len(args) > 3):
                self.__x = args[3]
            if (len(args) > 4):
                self.__y = args[4]
            return
        for key, value in kwargs.items():
            if hasattr(self, key) is True:
                setattr(self, key, value)

    def to_dictionary(self):
        """ to_dictionary"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
