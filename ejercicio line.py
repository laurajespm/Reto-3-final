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
            return Point (self.start.x, 0)
            
        if self.start.y == 0 and self.end.y == 0:
            print ("El cruce horizontal es infinito pues la línea se encuentra sobre el eje x.")
            return None
            
        if (self.start.y == self.end.y):
            print ("La línea nunca cruza el eje x")
            return None
            
        m = self.calculate_m()
        return  Point ((self.start.x - (self.start.y / m)), 0)

    def compute_vertical_cross(self):   
        if self.start.y == self.end.y:
            return Point(0, self.start.y)
            
        if self.start.x == 0 and self.end.x == 0:
            print ("El cruce vertical es infinito, pues la línea se encuentra sobre el eje y.")
            return None
            
        if (self.start.x == self.end.x):
            print ("La línea nunca cruza el eje y")
            return None
            
        m = self.calculate_m()
        if m is None:
            return None
        return Point(0, (self.start.y - (m * self.start.x)))



        
