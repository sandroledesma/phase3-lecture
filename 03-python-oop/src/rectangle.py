# classes are blueprints
from typing import Any


class Rectangle: 
    # constructor -- function that builds the object 
    # objects have to be created inside of the constructor
    def __init__(self, width_param, height_param):
        self.width = width_param # self._width (underscore) makes it 'private'
        self.height = height_param

    # getter function
    def get_width(self):
        '''return the width'''
        return self._width

    # setter function
    def set_width(self, new_width):
        '''update the existing width'''
        if new_width > 0: # control type of data entered 
            self._width = new_width
        else:
            raise ValueError('width must be positive') 
            # raises an error or exceptions
        
    # make width a property, disguise the getter and setter as an attribute 
    width = property(get_width, set_width)

    # decorator @property - create a function name that includes the getter and setter
    @property
    def height(self):
        '''gets the height'''
        return self._height

    @height.setter
    def height(self, new_height):
            '''sets the height'''    
            if new_height > 0: 
                self.height = new_height
            else:
                raise ValueError('height must be positive') 

    # method -- functions attached to a class
    def get_area(self):
        return self.width * self.height

    def get_circumference(self):
        return (2 * self.width) + (2 * self.height)
    
    # this gets called when you print the object
    def __repr__(self):
        return f'<Rectangle w:{self.width}, h:{self.height}>'
        # prints as "<Rectangle w:2, h:3>>"

# build a rectangle object
r1 = Rectangle(2, 3)
r2 = Rectangle(6, 9)

print(r1.width, r1.height, r1.get_area())

