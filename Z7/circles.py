from points import Point
import math
import unittest

class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self): 
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * pow(self.radius, 2)

    def move(self, x, y):
        self.pt.x += x
        self.pt.y += y

        return self

    def cover(self, other): 
       
        distance_x = self.pt.x - other.pt.x
        distance_y = self.pt.y - other.pt.y
        distance = math.sqrt(pow(distance_x, 2) + pow(distance_y, 2))

    
        if distance == 0:
            return Circle(self.pt.x, self.pt.y, max(self.radius, other.radius))

        # zaokraglam wyniki do 3 miejsc po przecinku
        new_radius = round((distance + self.radius + other.radius) / 2, 3) 
        scale = round((new_radius - self.radius) / distance, 3)
        new_x = round(self.pt.x + scale * (other.pt.x - self.pt.x), 3)
        new_y = round(self.pt.y + scale * (other.pt.y - self.pt.y), 3)

        return Circle(new_x, new_y, new_radius)



class TestCircle(unittest.TestCase):

    def test_init(self):
        
        with self.assertRaises(ValueError):
            c_1 = Circle(6, 5, -50)
            c_2 = Circle(4, 2, -0)
            c_3 = Circle(1.01, 3, -0.99)


    def test_repr(self):
        c_1 = Circle(6, 2, 7)
        c_2 = Circle(-2, 4, 1)
        c_3 = Circle(4.04, 2.1, 9.54)

        self.assertEqual(repr(c_1), "Circle(6, 2, 7)")
        self.assertEqual(repr(c_2), "Circle(-2, 4, 1)")
        self.assertEqual(repr(c_3), "Circle(4.04, 2.1, 9.54)")


    def test_eq(self):
        c_1 = Circle(2, 3, 5)
        c_2 = Circle(-2, 3, 5)
        c_3 = Circle(4.08, 3.5, 7)
        c_4 = Circle(4.08, 3.5, 7)
        c_5 = Circle(-2, 3, 5)

        self.assertTrue(c_2 == c_5)
        self.assertTrue(c_4 == c_3)
        self.assertTrue(c_3 == c_3)

        self.assertFalse(c_1 == c_2)
        self.assertFalse(c_3 == c_5)
    
    def test_ne(self):
        c_1 = Circle(2, 3, 5)
        c_2 = Circle(-2, 3, 5)
        c_3 = Circle(4.08, 3.5, 7)
        c_4 = Circle(4.08, 3.5, 7)
        c_5 = Circle(-2, 3, 5)

        self.assertFalse(c_2 != c_5)
        self.assertFalse(c_4 != c_3)
        self.assertFalse(c_3 != c_3)

        self.assertTrue(c_1 != c_2)
        self.assertTrue(c_3 != c_5)

    def test_area(self):
        c_1 = Circle(1, 0, 0)
        c_2 = Circle(4, 4, 5)
        c_3 = Circle(3.38, 4.4, 5.77)
        c_4 = Circle(-2, 3.03, 18)

        self.assertEqual(c_1.area(), 0)
        self.assertNotEqual(c_2.area(), 100)

        self.assertAlmostEqual(c_2.area(), 78.5, places = 1)
        self.assertAlmostEqual(c_3.area(), 104.539706, places = 0)
        self.assertAlmostEqual(c_4.area(), 1017.36, delta = 0.6) # roznica miedzy wynikami nie wieksza niz 0.6
    
    def test_move(self):
        c_1 = Circle(-1, 1, 1)
        c_2 = Circle(7, -23, 75)
        c_3 = Circle(7.67, 12, 8.8)
        c_4 = Circle(349587, -129384, 4456)

        self.assertEqual(c_1.move(1, -1), Circle(0, 0, 1))
        self.assertEqual(c_2.move(5, 2.5), Circle(12, -20.5, 75))
        self.assertEqual(c_3.move(6.23, 67.54), Circle(13.9, 79.54, 8.8))
        self.assertEqual(c_4.move(-123874, 31222), Circle(225713, -98162, 4456))


        self.assertNotEqual(c_2.move(2, -5.68473), Circle(1, 1, 75))
    
    def test_cover(self):
        c_1 = Circle(6, 5, 7)
        c_2 = Circle(6, 5, 8)
        c_3 = Circle(-2.2, 6, 37)
        c_4 = Circle(-234, 458, 5.067)
        c_5 = Circle(7.01, 34, 55)

        self.assertEqual(c_1.cover(c_2), Circle(6, 5, 8))
        self.assertEqual(c_3.cover(c_2), Circle(-12.491, 7.255, 26.630))
        self.assertEqual(c_4.cover(c_1), Circle(-113.52, 230.594, 262.358))
        self.assertEqual(c_5.cover(c_3), Circle(5.214, 28.540, 60.738))

        self.assertNotEqual(c_2.cover(c_1), Circle(0, 0, 8))


if __name__ == '__main__':
    unittest.main()
