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


if __name__ == "__main__":

    shape = Rectangle(20, 30)

    print(shape.length)
    print(shape.width)
    print(shape.get_perimeter())
