#En clase había manifestado mi duda, pues originalmente usé decoradores 
# (en un artículo de medium que se encontraba en los repos de las clases
# hablaban sobre decoradores, por tal motivo está adjunto otro archivo
# con un nombre similar)
# Este es según kwargs, como fue solicitado:

import math

class Point:
    def __init__(self, x : float,y: float):
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


class Rectangle:
    def __init__ (self, *args, **kwargs):
        if "bottom_left" in kwargs:
            bottom_left = kwargs["bottom_left"]
            self.width = kwargs ["width"]
            self.height = kwargs["height"]
            self.__validate_data()
            
            center_x = bottom_left.x + self.width / 2
            center_y = bottom_left.y + self.height / 2
            self.center = Point(center_x, center_y)
            
        elif "center" in kwargs:
            self.center = kwargs["center"]
            self.width = kwargs ["width"]
            self.height = kwargs["height"]
            self.__validate_data()
            
        elif "bottom_left" in kwargs and "top_right" in kwargs:
            bottom_left = kwargs["bottom_left"]
            top_right = kwargs["top_right"]

            self.width = (abs(top_right.x-bottom_left.x))
            self.height = (abs(top_right.y-bottom_left.y))
            self.__validate_data()

            center_x = (bottom_left.x + top_right.x)/2
            center_y = (bottom_left.y + top_right.y)/2
            self.center = Point(center_x, center_y)

        elif "lines" in kwargs:
            lines = kwargs["lines"]

            if len(lines) != 4:
                raise ValueError("Deben ser 4 líneas, pues un rectángulo se compone de exactamente dicha cantidad.")
            
            for l in lines:
                if not isinstance(l,Line):
                    raise TypeError("Los elementos deben ser de tipo Line, no de otro tipo.")
            
            x_points = []
            y_points = []
            
            for l in lines:
                x_points.extend ([l.start.x, l.end.x])
                y_points.extend ([l.start.y, l.end.y])
            
            self.width = max(x_points) - min(x_points)
            self.height = max(y_points) - min(y_points)
            
            self.__validate_data()
            center_x = (max(x_points) + min(x_points)) / 2
            center_y = (max(y_points) + min(y_points)) / 2
            self.center = Point (center_x, center_y)
            self.lines = lines

        else:
            raise ValueError ("Formato no válido, no coincide con ninguno de los tres métodos.")
    
    def __validate_data(self):
        if self.width < 0 or self.height < 0:
            raise ValueError("El ancho o el alto no pueden ser negativos.")
        elif self.width == 0 or self.height == 0:
            raise ValueError("El ancho o el alto no pueden ser iguales a 0.")
    
    def compute_area(self):
        return self.width*self.height
    
    def compute_perimeter(self):
        return ((self.width*2)+(self.height*2))

    def compute_interference_point(self, point: Point):
        limit_1_x = (self.width / 2) + self.center.x
        limit_2_x = self.center.x - (self.width/2)
        limit_1_y = (self.height / 2) + self.center.y
        limit_2_y = self.center.y - (self.height / 2)

        return (point.x <= limit_1_x and point.x >=limit_2_x and point.y <= limit_1_y and point.y >= limit_2_y )
