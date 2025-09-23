import geometric_shapes

retangle = geometric_shapes.Rectangle(10, 20)
ellipse = geometric_shapes.Ellipse(9, 7)
square = geometric_shapes.Square(4)
circle = geometric_shapes.Circle(20)
complex_shape = geometric_shapes.ComplexShape(circle, [retangle, ellipse, square])
complex_shape_area = complex_shape.get_area()
complex_shape_edge_length = complex_shape.get_edge_length()
