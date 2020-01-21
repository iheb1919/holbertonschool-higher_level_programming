#!/usr/bin/python3

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise Exception("{} must be an integer".format(name))
        if value <= 0:
            raise Exception("{} must be an greater than 0".format(name))
