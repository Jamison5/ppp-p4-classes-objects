from math import pi
from math import sqrt
from utils import (
    InvalidArgumentError,
    validate_positive_number,
    validate_non_empty_string,
)


class GeometricShape:

    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Rectangle(GeometricShape):

    def __init__(self, length, width, name="Rectangle"):

        super().__init__(name)
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


class Ellipse(GeometricShape):

    def __init__(self, semi_major_axis, semi_minor_axis, name="Ellipse"):
        super().__init__(name)
        self.set_semi_major_axis(semi_major_axis)
        self.set_semi_minor_axis(semi_minor_axis)

    def get_semi_major_axis(self):
        return self.__semi_major_axis

    def set_semi_major_axis(self, semi_major_axis):
        self.__semi_major_axis = semi_major_axis

    def get_semi_minor_axis(self):
        return self.__semi_minor_axis

    def set_semi_minor_axis(self, semi_minor_axis):
        self.__semi_minor_axis = semi_minor_axis

    def get_perimeter(self):
        perimeter = pi * (
            3 * (self.__semi_major_axis + self.__semi_minor_axis)
            - sqrt(
                (3 * self.__semi_major_axis + self.__semi_minor_axis)
                * (self.__semi_major_axis + 3 * self.__semi_minor_axis)
            )
        )

        return perimeter

    def get_area(self):
        area = self.__semi_major_axis * self.__semi_minor_axis * pi
        return area


class Square(Rectangle):

    def __init__(self, side):

        super().__init__(side, side, name="Square")

    def get_side(self):
        return self.get_length()

    def set_side(self, side):
        self.set_length(side)
        self.set_width(side)


class Circle(Ellipse):

    def __init__(self, radius):

        super().__init__(radius, radius, name="Circle")

    def get_radius(self):
        return self.get_semi_major_axis()

    def set_radius(self, radius):
        self.set_semi_major_axis(radius)
        self.set_semi_minor_axis(radius)


if __name__ == "__main__":

    circle = Circle(10)
    print(circle.get_radius())
    circle.set_radius(20)
    print(circle.get_radius())
    print(circle._GeometricShape__name)
    print(circle.get_semi_major_axis())
    print(circle.get_perimeter())
    print(circle.get_area())
