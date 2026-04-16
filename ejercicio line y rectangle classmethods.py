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
        
    def calculate_m(self):
        if self.end.x == self.start.x:
            return None
        return ((self.end.y - self.start.y)/(self.end.x - self.start.x))
            
    def compute_length(self):
        self.length = math.hypot((self.end.x - self.start.x),(self.end.y - self.start.y))
        return self.length
    
    def compute_slope(self):
        m = self.calculate_m()
        if m is None:
            self.slope = 90
        else:
            self.slope = math.degrees(math.atan(m))
        return self.slope
    
    def compute_horizontal_cross(self):
        if self.end.x == self.start.x:
            return Point(self.start.x, 0)
            
        if self.start.y == 0 and self.end.y == 0:
            print("El cruce horizontal es infinito pues la línea se encuentra sobre el eje x.")
            return None
            
        if self.start.y == self.end.y:
            print("La línea nunca cruza el eje x")
            return None
            
        m = self.calculate_m()
        
        if m is None:
            return None
            
        return Point((self.start.x - (self.start.y / m)), 0)

    def compute_vertical_cross(self):   
        if self.start.y == self.end.y:
            return Point(0, self.start.y)
            
        if self.start.x == 0 and self.end.x == 0:
            print("El cruce vertical es infinito, pues la línea se encuentra sobre el eje y.")
            return None
            
        if self.start.x == self.end.x:
            print("La línea nunca cruza el eje y")
            return None
            
        m = self.calculate_m()
        
        if m is None:
            return None
            
        return Point(0, (self.start.y - (m * self.start.x)))


class Rectangle:
    def __init__(self, width: float, height: float, center: Point):
        if width <= 0 or height <= 0:
            raise ValueError("La altura o el ancho de un rectángulo no pueden ser iguales a 0.")
        self.width = width
        self.height = height
        self.center = center

    @classmethod
    def method_1(cls, bottom_left: Point, width: float, height: float):
        center = Point(bottom_left.x + width/2, bottom_left.y + height/2)
        return cls(width, height, center)

    @classmethod
    def method_2(cls, width: float, height: float, center: Point):
        return cls(width, height, center)

    @classmethod
    def method_3(cls, bottom_left: Point, top_right: Point):
        width = abs(top_right.x - bottom_left.x)
        height = abs(top_right.y - bottom_left.y)
        center = Point((bottom_left.x + top_right.x)/2, (bottom_left.y + top_right.y)/2)
        return cls(width, height, center)

    @classmethod
    def method_4(cls, l1: Line, l2: Line, l3: Line, l4: Line):
        x_points = [l1.start.x, l1.end.x, l2.start.x, l2.end.x, l3.start.x, l3.end.x, l4.start.x, l4.end.x]
        y_points = [l1.start.y, l1.end.y, l2.start.y, l2.end.y, l3.start.y, l3.end.y, l4.start.y, l4.end.y]
        width = max(x_points) - min(x_points)
        height = max(y_points) - min(y_points)
        center = Point((max(x_points) + min(x_points))/2, (max(y_points) + min(y_points))/2)
        return cls(width, height, center)

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2*(self.width + self.height)

    def compute_interference_point(self, point: Point):
        return (point.x <= self.center.x + self.width/2 and point.x >= self.center.x - self.width/2 and point.y <= self.center.y + self.height/2 and point.y >= self.center.y - self.height/2)



class Square(Rectangle):
    def __init__(self, side: float, center: Point):
        super().__init__(side, side, center)