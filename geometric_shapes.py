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


if __name__ == "__main__":

    ellipse = Ellipse(10, 5)
    print(ellipse.get_semi_major_axis())

    ellipse.set_semi_major_axis(20)
    print(ellipse.get_semi_major_axis())

    print(ellipse.get_semi_minor_axis())

    ellipse.set_semi_minor_axis(10)
    print(ellipse.get_semi_minor_axis())

    print(ellipse._Ellipse__semi_major_axis)

    print(ellipse.semi_major_axis)
