import math

class Point:
    def __init__ (self, x : float,y: float):
        self.x= x
        self.y= y
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = 0
        self.slope = 0
    #preguntar: ¿Podría acá usar una property de length?
    def compute_length(self):
        return math.hypot((self.end.x - self.start.x),(self.end.y - self.start.y))
    
    def compute_slope(self):
        if (self.end.x - self.start.x) == 0:
            print ("La pendiente es indefinida, pues se trata de una línea vertical.")
            return None
        else:
            return ((self.end.y - self.start.y)/(self.end.x - self.start.x))
    
    def compute_horizontal_cross(self):
        m = self.compute_slope()
        if self.start.y == 0 and self.end.y == 0:
            print ("El cruce horizontal es infinito pues la línea se encuentra sobre el eje x.")
            return None
        if (self.start.y == self.end.y):
            print ("La línea nunca cruza el eje x")
            return None
        if self.end.x == self.start.x:
            return Point (self.start.x, 0)
        return  Point ((self.start.x - (self.start.y / m)), 0)

    def compute_vertical_cross(self):
        m = self.compute_slope()
        if self.start.x == 0 and self.end.x == 0:
            print ("El cruce vertical es infinito, pues la línea se encuentra sobre el eje y.")
            return None
        if (self.start.x == self.end.x):
            print ("La línea nunca cruza el eje y")
            return None
        return Point(0, (self.start.y - (m * self.start.x)))

        