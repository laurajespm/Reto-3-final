#En clase había manifestado mi duda, pues originalmente usé decoradores 
# (en un artículo de medium que se encontraba en las clases hablaban 
# sobre decoradores, por tal motivo lo usé)
# Este es según kwargs, como solicitaste:

import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = 0
        self.slope = 0

    def compute_length(self):
        self.length = math.hypot(
            (self.end.x - self.start.x),
            (self.end.y - self.start.y)
        )
        return self.length

    def compute_slope(self):
        if (self.end.x - self.start.x) == 0:
            print("La pendiente es indefinida, pues se trata de una línea vertical.")
            return None
        else:
            self.slope = ((self.end.y - self.start.y) /
                          (self.end.x - self.start.x))
            return self.slope

    def compute_horizontal_cross(self):
        m = self.compute_slope()

        if self.start.y == 0 and self.end.y == 0:
            print("El cruce horizontal es infinito pues la línea se encuentra sobre el eje x.")
            return None

        if self.start.y == self.end.y:
            print("La línea nunca cruza el eje x")
            return None

        if self.end.x == self.start.x:
            return Point(self.start.x, 0)

        return Point(self.start.x - (self.start.y / m), 0)

    def compute_vertical_cross(self):
        m = self.compute_slope()

        if self.start.x == 0 and self.end.x == 0:
            print("El cruce vertical es infinito, pues la línea se encuentra sobre el eje y.")
            return None

        if self.start.x == self.end.x:
            print("La línea nunca cruza el eje y")
            return None

        return Point(0, (self.start.y - (m * self.start.x)))


class Rectangle:
    def __init__(self, width: float = 0, height: float = 0, center=None, **kwargs):

        if "lines" in kwargs:
            lines = kwargs["lines"]

            x_points = []
            y_points = []

            for line in lines:
                x_points.append(line.start.x)
                x_points.append(line.end.x)
                y_points.append(line.start.y)
                y_points.append(line.end.y)

            width = max(x_points) - min(x_points)
            height = max(y_points) - min(y_points)

            center = Point(
                (max(x_points) + min(x_points)) / 2,
                (max(y_points) + min(y_points)) / 2
            )

        elif "bottom_left" in kwargs and "bottom_right" in kwargs:
            bl = kwargs["bottom_left"]
            br = kwargs["bottom_right"]

            width = abs(br.x - bl.x)
            height = abs(br.y - bl.y)

            center = Point(
                (bl.x + br.x) / 2,
                (bl.y + br.y) / 2
            )

        elif "bottom_left" in kwargs and "width" in kwargs and "height" in kwargs:
            bl = kwargs["bottom_left"]

            width = kwargs["width"]
            height = kwargs["height"]

            center = Point(
                bl.x + width / 2,
                bl.y + height / 2
            )

        else:
            center = center if center is not None else Point(0, 0)

        if width < 0:
            print("El ancho no puede ser negativo")

        if height < 0:
            print("La altura no puede ser negativa")

        self.width = width
        self.height = height
        self.center = center

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def compute_interference_point(self, point: Point):
        limit_1_x = (self.width / 2) + self.center.x
        limit_2_x = self.center.x - (self.width / 2)
        limit_1_y = (self.height / 2) + self.center.y
        limit_2_y = self.center.y - (self.height / 2)

        return (
            point.x <= limit_1_x and point.x >= limit_2_x and
            point.y <= limit_1_y and point.y >= limit_2_y
        )


class Square(Rectangle):
    def __init__(self, side: float, center=None):
        super().__init__(side, side, center)