from points import Point
import unittest

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

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


class TestTriangle(unittest.TestCase):

    def setUp(self): #aby testowanie funkcji typu move() nie zmienialo wartosci triangle_x
        self.triangle_1 = Triangle(4, 2, 1, 3, -1, -6)
        self.triangle_2 = Triangle(5, 5, -3, 2, 0, 0)
        self.triangle_3 = Triangle(-50, -25, 0, 37, 48, -13)
        self.triangle_4 = Triangle(-5.50, -10.255, 9, 8.34, 5, -17.9)
        self.triangle_5 = Triangle(-50, -25, 0, 37, 48, -13)

    def test_str(self):
        self.assertEqual(str(self.triangle_1), "[(4, 2), (1, 3), (-1, -6)]")
        self.assertEqual(str(self.triangle_2), "[(5, 5), (-3, 2), (0, 0)]")
        self.assertEqual(str(self.triangle_3), "[(-50, -25), (0, 37), (48, -13)]")
        self.assertEqual(str(self.triangle_4), "[(-5.5, -10.255), (9, 8.34), (5, -17.9)]")
        self.assertEqual(str(self.triangle_5), "[(-50, -25), (0, 37), (48, -13)]")

    def test_repr(self):
        self.assertEqual(repr(self.triangle_1), "Triangle(4, 2, 1, 3, -1, -6)")
        self.assertEqual(repr(self.triangle_2), "Triangle(5, 5, -3, 2, 0, 0)")
        self.assertEqual(repr(self.triangle_3), "Triangle(-50, -25, 0, 37, 48, -13)")
        self.assertEqual(repr(self.triangle_4), "Triangle(-5.5, -10.255, 9, 8.34, 5, -17.9)")
        self.assertEqual(repr(self.triangle_5), "Triangle(-50, -25, 0, 37, 48, -13)")

    def test_eq(self):
        self.assertTrue(self.triangle_3 == self.triangle_5)
        self.assertTrue(self.triangle_1 == self.triangle_1)
        self.assertTrue(self.triangle_4 == Triangle(-5.50, -10.255, 9, 8.34, 5, -17.9)) 

        self.assertFalse(self.triangle_2 == self.triangle_4)
        self.assertFalse(self.triangle_1 == self.triangle_2)

        with self.assertRaises(TypeError):
            self.triangle_3 == "abc"


    def test_ne(self):
        self.assertTrue(self.triangle_5 != self.triangle_1)
        self.assertTrue(self.triangle_4 != Triangle(0, 0, 0, 0, 0, 0))
        self.assertTrue(self.triangle_2 != self.triangle_3)
        
        self.assertFalse(self.triangle_2 != Triangle(5, 5, -3, 2, 0, 0))
        self.assertFalse(self.triangle_4 != self.triangle_4)
        self.assertFalse(self.triangle_5 != self.triangle_3)

        with self.assertRaises(TypeError):
            self.triangle_3 != "xyz"

    def test_center(self):
        self.assertEqual(self.triangle_1.center(), Point(1.33333, -0.33333))
        self.assertEqual(self.triangle_2.center(), Point(0.66667, 2.33333))
        self.assertEqual(self.triangle_4.center(), Point(2.83333, -6.605))

        self.assertNotEqual(self.triangle_5.center(), Point(0.45, 1.12))
        self.assertNotEqual(self.triangle_1.center(), Point(0, 0))


    def test_area(self):
        self.assertAlmostEqual(self.triangle_1.area(), 14.5, places=1)
        self.assertEqual(self.triangle_3.area(), 2738) 
        self.assertAlmostEqual(self.triangle_4.area(), 153.05, places=2)
        self.assertAlmostEqual(self.triangle_2.area(), 12.5, places=1) 

        self.assertNotAlmostEqual(self.triangle_1.area(), 20.0, places=1)
        self.assertNotEqual(self.triangle_3.area(), 4958392)
        self.assertNotAlmostEqual(self.triangle_4.area(), 100.0, places=2)
        self.assertNotEqual(self.triangle_2.area(), 0)          

    def test_move(self):
       
        self.triangle_1.move(1, -1)
        self.assertEqual(self.triangle_1, Triangle(5, 1, 2, 2, 0, -7))
    
        self.triangle_2.move(-2, 3)
        self.assertEqual(self.triangle_2, Triangle(3, 8, -5, 5, -2, 3))
    
        self.triangle_3.move(10, 10)
        self.assertEqual(self.triangle_3, Triangle(-40, -15, 10, 47, 58, -3))
    
        self.triangle_4.move(0, 0)
        self.assertEqual(self.triangle_4, Triangle(-5.5, -10.255, 9, 8.34, 5, -17.9))
    
        self.triangle_5.move(-2.5, 4.75)
        self.assertEqual(self.triangle_5, Triangle(-52.5, -20.25, -2.5, 41.75, 45.5, -8.25))



if __name__ == '__main__':
    unittest.main()
