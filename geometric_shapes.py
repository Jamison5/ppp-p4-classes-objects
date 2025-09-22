from math import pi
from math import sqrt


class GeometricShape:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        perimeter = (2 * self.length) + (2 * self.width)
        return perimeter

    def get_area(self):
        area = self.length * self.width
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

    geometric_shape = GeometricShape("Triangle")
    print(geometric_shape.name)

    rectangle = Rectangle(10, 20)
    print(rectangle.get_perimeter())
    print(rectangle.get_area())

    ellipse = Ellipse(20, 10)
    print(ellipse.get_perimeter())
    print(ellipse.get_area())
