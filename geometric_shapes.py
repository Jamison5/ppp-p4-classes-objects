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

    def __repr__(self):
        return f"GeometricShape(name={self.__name})"

    def __eq__(self, other):
        return repr(self) == repr(other)


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

    def __repr__(self):
        return f"Rectangle(a={self.get_length()}, b={self.get_width()})"

    def __eq__(self, other):
        return repr(self) == repr(other)


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

    def __repr__(self):
        return f"Ellipse(r1={self.__semi_major_axis}, r2={self.__semi_minor_axis})"

    def __eq__(self, other):
        return repr(self) == repr(other)


class Square(Rectangle):

    def __init__(self, side):

        super().__init__(side, side, name="Square")

    def get_side(self):
        return self.get_length()

    def set_side(self, side):
        self.set_length(side)
        self.set_width(side)

    def __repr__(self):
        return f"Square(a={self.get_length()})"

    def __eq__(self, other):
        return repr(self) == repr(other)


class Circle(Ellipse):

    def __init__(self, radius):

        super().__init__(radius, radius, name="Circle")

    def get_radius(self):
        return self.get_semi_major_axis()

    def set_radius(self, radius):
        self.set_semi_major_axis(radius)
        self.set_semi_minor_axis(radius)

    def __repr__(self):
        return f"Circle(r={self.get_semi_major_axis()})"

    def __eq__(self, other):
        return repr(self) == repr(other)


class ComplexShape(GeometricShape):
    def __init__(self, base, holes):
        super().__init__("ComplexShape")
        self.__base = base

        if isinstance(holes, list):
            self.__holes = holes
        else:
            self.__holes = [holes]

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def get_holes(self):
        return self.__holes

    def set_holes(self, holes):
        self.__holes = holes

    def add_hole(self, hole):
        if isinstance(hole, list):
            for item in hole:
                self.__holes.append(item)

        else:
            self.__holes.append(hole)

    def remove_hole(self, hole):
        self.__holes.remove(hole)

    def get_area(self):
        base_area = self.__base.get_area()
        holes_area = sum(h.get_area() for h in self.__holes)
        return base_area - holes_area

    def get_edge_length(self):
        base_edge = self.__base.get_perimeter()
        holes_edge = sum(h.get_perimeter() for h in self.__holes)
        return base_edge + holes_edge

    def __repr__(self):
        return f"ComplexShape({self.__base.get_name()} with {len(self.__holes)} holes)"


if __name__ == "__main__":

    # shape = Rectangle(5, 10)
    # shape.set_length(10)
    # print(shape.get_length())
    # print("-----------------")
    # shape.set_width(5)
    # print(shape.get_width())
    # print("-----------------")
    # shape.set_width("Hello")

    # base = Ellipse(20, 10)
    # hole1 = Square(5)
    # hole2 = Circle(3)
    # complex_shape = ComplexShape(base, hole1)
    # print(complex_shape.get_holes())
    # print("----" * 5)
    # complex_shape.add_hole(hole2)
    # print(complex_shape.get_holes())
    # print("----" * 5)
    # complex_shape.remove_hole(hole1)
    # print(complex_shape.get_holes())
    # print("----" * 5)
    # print(complex_shape.get_area())
    # print("----" * 5)
    # print(complex_shape.get_edge_length())

    # base = Square(10)  # The base shape
    # square1 = Square(5)
    # rectangle1 = Rectangle(3, 4)
    # square2 = Square(6)  # This is the one we'll try to remove
    # rectangle2 = Rectangle(2, 7)

    # # Create the ComplexShape with the same structure
    # test_obj = ComplexShape(base, [square1, rectangle1, square2, rectangle2])

    # print("Initial holes:")
    # for i, hole in enumerate(test_obj.get_holes()):
    #     print(f"  {i}: {type(hole).__name__} at {hex(id(hole))}")

    # print(f"\nTrying to remove square2 at {hex(id(square2))}")
    # print(f"square2 object: {square2}")

    # # This should remove square2 and leave [square1, rectangle1, rectangle2]
    # test_obj.remove_hole(square2)

    # print("\nAfter removal:")
    # for i, hole in enumerate(test_obj.get_holes()):
    #     print(f"  {i}: {type(hole).__name__} at {hex(id(hole))}")

    # print(f"\nExpected 3 holes, got {len(test_obj.get_holes())} holes")
    # print("Expected to keep: square1, rectangle1, rectangle2")
    # print("Expected to remove: square2")

    geometric_shape = GeometricShape("Triangle")
    geometric_shape2 = GeometricShape("Triangle")
    geometric_shape3 = GeometricShape("Square")
    print(geometric_shape)
    print(geometric_shape == geometric_shape2)
    print(geometric_shape == geometric_shape3)

    square = Square(5)
    print(square)

    ellipse = Ellipse(5, 3)
    print(ellipse)

    circle = Circle(5)
    print(circle)

    base = Square(100)
    holes = [Circle(10), Circle(5)]
    complex_shape = ComplexShape(base, holes)
    print(complex_shape)
