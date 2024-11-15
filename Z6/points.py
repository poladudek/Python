import unittest
import math #dla pow() i sqrt()

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


class TestPoint(unittest.TestCase):

    def test_str(self):
        point_1 = Point(2, 2)
        self.assertEqual(point_1.__str__(), "(2, 2)")

        point_2 = Point(-4, -5867482938)
        self.assertEqual(point_2.__str__(), "(-4, -5867482938)")
        self.assertEqual(str(point_2), "(-4, -5867482938)")


    def test_repr(self):
        point_1 = Point(485759, 987413)
        self.assertEqual(point_1.__repr__(), "Point(485759, 987413)")

        point_2 = Point(-1000000, -10000000000)
        self.assertEqual(point_2.__repr__(), "Point(-1000000, -10000000000)")
        self.assertEqual(repr(point_2), "Point(-1000000, -10000000000)")

    def test_eq(self):
        point_1 = Point(7, 8)
        point_2 = Point(-7, -8)
        point_3 = Point(7, 8)
        point_4 = Point(0, 0)
        point_5 = Point(0, 0)
        point_6 = (7, 8)

        self.assertFalse(point_1.__eq__(point_2))
        self.assertFalse(point_1.__eq__(point_4))
        self.assertTrue(point_3.__eq__(point_1))
        self.assertTrue(point_5.__eq__(point_4))
        self.assertTrue(point_1.__eq__(point_1))

        self.assertTrue(point_4 == point_5)
        self.assertFalse(point_2 == point_1)

        with self.assertRaises(TypeError):
            point_1 == point_6

    def test_ne(self):
        point_1 = Point(-4, 3)
        point_2 = Point(5, 87)
        point_3 = Point(3, -4)
        point_4 = Point(5, 87)

        self.assertTrue(point_2.__ne__(point_3))
        self.assertFalse(point_4.__ne__(point_4))
        self.assertFalse(point_2.__ne__(point_4))
        
        self.assertTrue(point_1 != point_3)
        self.assertTrue(point_2 != (point_3))

    def test_add(self):
        point_1 = Point(-1, 2)
        point_2 = Point(1, -2)
        point_3 = Point(5, 7)
        point_4 = Point(33.33, 12.57)
        point_5 = Point(67.98, 25.12)

        self.assertEqual(point_1.__add__(point_2), Point(0, 0))
        self.assertEqual(point_3.__add__(point_1), Point(4, 9))
        self.assertEqual(point_5.__add__(point_4), Point(101.31, 37.69))

        self.assertNotEqual(point_4.__add__(point_3), Point(55, 14))

        self.assertEqual(point_5 + point_1, Point(66.98, 27.12))
        self.assertEqual(point_1 + point_2, Point(0, 0))

    def test_sub(self):
        point_1 = Point(-57.12, -1.09)
        point_2 = Point(-8, -12.034)
        point_4 = Point(5, 8)
        point_5 = Point(12, -3.3)

        self.assertEqual(point_1.__sub__(point_2), Point(-49.12, 10.944))
        self.assertEqual(point_4.__sub__(point_1), Point(62.12, 9.09))
        self.assertEqual(point_5.__sub__(point_4), Point(7.00, -11.3))

        self.assertNotEqual(point_1 - point_2, Point(-48.00, 18.000))

        self.assertEqual(point_4 - point_1, Point(62.12, 9.09))
        self.assertEqual(point_4 - point_5, Point(-7, 11.3))

    def test_mul(self):
        point_1 = Point(3, 6)
        point_2 = Point(-5, 0)
        point_3 = Point(3.5, -1.09)
        point_4 = Point(6.025, 3.1)

        self.assertEqual(point_1.__mul__(point_2), -15)
        self.assertEqual(point_3.__mul__(point_4), 17.7085)

        self.assertEqual(point_2 * point_3, -17.5)
        self.assertEqual(point_3 * point_4, 17.7085)

    def test_cross(self):
        point_1 = Point(4, 6)
        point_2 = Point(5.5, 6.748374)
        point_3 = Point(-12, 472.5837)

        self.assertEqual(point_1.cross(point_2), -6.006504)

        self.assertAlmostEqual(point_1.cross(point_2), -6, places=0)
        self.assertAlmostEqual(point_3.cross(point_2), -2680.190838, 6)
        

    def test_length(self):
        point_1 = Point(3, 4)
        point_2 = Point(4, 4)
        point_3 = Point(-1, 6)
        point_4 = Point(1, -6)

        self.assertEqual(point_1.length(), 5)
        self.assertAlmostEqual(point_2.length(), 5.66, 2)
        self.assertAlmostEqual(point_3.length(), 6.08276, places = 5)
        self.assertAlmostEqual(point_4.length(), 6.08276, places = 5)


if __name__ == '__main__':
    unittest.main()
