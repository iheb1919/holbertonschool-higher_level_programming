#!/usr/bin/python3
"""
class square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
        Attr:
           size(getter/setter)
       Class constructor:
           def __init__(self, size, x=0, y=0, id=None)

    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """__str__ """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ update """
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass
        for key, value in kwargs.items():
            if hasattr(self, key) is True:
                setattr(self, key, value)

    def to_dictionary(self):
        """ to_dictionary"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
