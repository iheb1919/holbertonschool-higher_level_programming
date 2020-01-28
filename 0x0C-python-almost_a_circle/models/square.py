#!/usr/bin/python3
"""
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """The getter function"""
        return self.width

    @size.setter
    def size(self, value):
        """The setter function for the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """The overloading __str__ method """
        return "[Square] ({}) {}/{} - {}"
        .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
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
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
