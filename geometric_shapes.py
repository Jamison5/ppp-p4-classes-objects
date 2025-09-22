from math import pi
from math import sqrt


class GeometricShape:

    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Rectangle:

    def __init__(self, length, width):
        self.set_length(length)
        self.set_width(width)

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_perimeter(self):
        perimeter = (2 * self.__length) + (2 * self.__width)
        return perimeter

    def get_area(self):
        area = self.__length * self.__width
        return area


class Ellipse:

    def __init__(self, semi_major_axis, semi_minor_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def get_perimeter(self):
        perimeter = pi * (
            3 * (self.semi_major_axis + self.semi_minor_axis)
            - sqrt(
                (3 * self.semi_major_axis + self.semi_minor_axis)
                * (self.semi_major_axis + 3 * self.semi_minor_axis)
            )
        )

        return perimeter

    def get_area(self):
        area = self.semi_major_axis * self.semi_minor_axis * pi
        return area


if __name__ == "__main__":

    rectangle = Rectangle(5, 10)
    print(rectangle.get_length())

    rectangle.set_length(10)
    print(rectangle.get_length())

    print(rectangle.get_width())

    rectangle.set_width(20)
    print(rectangle.get_width())

    print(rectangle._Rectangle__length)

    print(rectangle.length)
