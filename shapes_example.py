from geometric_shapes import Rectangle, Ellipse, Square, Circle, ComplexShape

rectangle = Rectangle(10, 20)
ellipse = Ellipse(9, 7)
square = Square(4)
circle = Circle(20)
complex_shape = ComplexShape(circle, [rectangle, ellipse, square])
complex_shape_area = complex_shape.get_area()
complex_shape_edge_length = complex_shape.get_edge_length()

if __name__ == "__main__":
    print(complex_shape.get_holes())
    complex_shape.remove_hole(ellipse)
    print(complex_shape.get_holes())
