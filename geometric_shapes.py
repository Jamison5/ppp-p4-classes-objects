from math import pi
from math import sqrt
from utils import (
    validate_positive_number,
    validate_non_empty_string,
)


class GeometricShape:

    def __init__(self, name):
        validate_non_empty_string(name)
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        validate_non_empty_string(name)
        self.__name = name


class Rectangle(GeometricShape):

    def __init__(self, length, width, name="Rectangle"):

        super().__init__(name)
        validate_positive_number(length)
        self.set_length(length)
        validate_positive_number(width)
        self.set_width(width)

    def get_length(self):
        return self.__length

    def set_length(self, length):
        validate_positive_number(length)
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        validate_positive_number(width)
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
        validate_positive_number(semi_major_axis)
        self.set_semi_major_axis(semi_major_axis)
        validate_positive_number(semi_minor_axis)
        self.set_semi_minor_axis(semi_minor_axis)

    def get_semi_major_axis(self):
        return self.__semi_major_axis

    def set_semi_major_axis(self, semi_major_axis):
        validate_positive_number(semi_major_axis)
        self.__semi_major_axis = semi_major_axis

    def get_semi_minor_axis(self):
        return self.__semi_minor_axis

    def set_semi_minor_axis(self, semi_minor_axis):
        validate_positive_number(semi_minor_axis)
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


class ComplexShape(GeometricShape):

    def __init__(self, base, holes, name="ComplexShape"):
        super().__init__(name)
        self.set_base(base)
        self.set_holes(holes)

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def get_holes(self):
        return self.__holes

    def set_holes(self, holes):

        if isinstance(holes, list):
            self.__holes = holes

        self.__holes = [holes]

    def add_hole(self, hole):
        self.__holes.append(hole)

    def remove_hole(self, hole):
        self.__holes.remove(hole)

    def get_area(self):
        area_of_holes = 0
        for hole in self.__holes:
            area_of_holes += hole.get_area()
        complex_area = self.__base.get_area() - area_of_holes
        return complex_area

    def get_edge_length(self):
        edge_length_of_holes = 0
        for hole in self.__holes:
            edge_length_of_holes += hole.get_perimeter()
        edge_length_of_shape = self.__base.get_perimeter() + edge_length_of_holes
        return edge_length_of_shape


if __name__ == "__main__":

    # shape = Rectangle(5, 10)
    # shape.set_length(10)
    # print(shape.get_length())
    # print("-----------------")
    # shape.set_width(5)
    # print(shape.get_width())
    # print("-----------------")
    # shape.set_width("Hello")

    base = Ellipse(20, 10)
    hole1 = Square(5)
    hole2 = Circle(3)
    complex_shape = ComplexShape(base, hole1)
    print(complex_shape.get_holes())
    print("----" * 5)
    complex_shape.add_hole(hole2)
    print(complex_shape.get_holes())
    print("----" * 5)
    complex_shape.remove_hole(hole1)
    print(complex_shape.get_holes())
    print("----" * 5)
    print(complex_shape.get_area())
    print("----" * 5)
    print(complex_shape.get_edge_length())
