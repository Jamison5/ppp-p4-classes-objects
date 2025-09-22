class GeometricShape:

    def __init__(self, name):
        self.name = name


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


if __name__ == "__main__":

    ellipse = Ellipse(20, 10)

    print(ellipse.semi_major_axis)

    print(ellipse.semi_minor_axis)

    print("------")

    ellipse.semi_major_axis = 40

    print(ellipse.semi_major_axis)

    ellipse.semi_minor_axis = 30

    print(ellipse.semi_minor_axis)
