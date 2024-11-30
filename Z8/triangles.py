from points import Point

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
    
    def from_points(points):
        if( isinstance(points, tuple)):
            points = list(points)

        return Triangle(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x, points[2].y) #zawieraja obiekty Point

    def __str__(self): 
        return (f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]")

    def __repr__(self):
        return (f"Triangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y}, {self.pt3.x}, {self.pt3.y})")

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError("Not a Triangle")
            return False
        triangle_1_set = {(self.pt1.x, self.pt1.y), (self.pt2.x, self.pt2.y), (self.pt3.x, self.pt3.y)} #uzywam setow, skoro kolejnosc punktow nie ma znaczenia
        triangle_2_set = {(other.pt1.x, other.pt1.y), (other.pt2.x, other.pt2.y), (other.pt3.x, other.pt3.y)}
        return triangle_1_set == triangle_2_set

    def __ne__(self, other):
        return not (self == other)

    @property
    def center(self):
        mass_center_x = round((self.pt1.x + self.pt2.x + self.pt3.x) / 3, 5)
        mass_center_y = round((self.pt1.y + self.pt2.y + self.pt3.y) / 3, 5)
        return Point(mass_center_x, mass_center_y)

    def area(self):
        return (1/2) * abs(self.pt1.x * (self.pt2.y - self.pt3.y) +  self.pt2.x * (self.pt3.y - self.pt1.y) + self.pt3.x * (self.pt1.y - self.pt2.y))

    def move(self, x, y):
        for parameter in [self.pt1, self.pt2, self.pt3]:
            parameter.x += x
            parameter.y += y

    @property
    def top(self):
        return max([self.pt1.y, self.pt2.y, self.pt3.y])

    @property
    def bottom(self):
        return min([self.pt1.y, self.pt2.y, self.pt3.y])

    @property
    def left(self):
        return min([self.pt1.x, self.pt2.x, self.pt3.x])

    @property
    def right(self):
        return max([self.pt1.x, self.pt2.x, self.pt3.x])

    
    @property
    def height(self):
        return self.top - self.bottom
    
    @property
    def width(self):
        return self.right - self.left

    
    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)   
    
    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bounding_box(self): #dodatkowo funkcja dla bounding box prostokata
        return (self.bottomleft, self.bottomright, self.topleft, self.topright)
