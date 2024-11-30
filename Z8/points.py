import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise TypeError("Not a Point")
            return False
        if self.x == other.x and self.y == other.y:
            return True 
        return False 

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y 
        return Point(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y 
        return Point(new_x, new_y)


    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


    def cross(self, other): 
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def __hash__(self):
        return hash((self.x, self.y))

