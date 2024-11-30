import pytest
from triangles import Triangle
from points import Point


class TestTriangles:
    def setup_method(self):
        self.triangle_1 = Triangle(4, 2, 1, 3, -1, -8)
        self.triangle_2 = Triangle(5, 5, -3, 2, 0, 0)
        self.triangle_3 = Triangle(-50, -25, 0, 37, 48, -13)
        self.triangle_4 = Triangle(-5.5, -10.255, 9, 8.34, 5, -17.9)
        self.triangle_5 = Triangle(-50, -25, 0, 37, 48, -13)

    def test_from_points(self):
        
        p1 = Point(4, 2)
        p2 = Point(1, 3)
        p3 = Point(-1, -8)
        
        triangle_fp1 = Triangle.from_points((p1, p2, p3))

        assert triangle_fp1.pt1.x == 4
        assert triangle_fp1.pt1.y == 2
        assert triangle_fp1.pt2.x == 1
        assert triangle_fp1.pt2.y == 3
        assert triangle_fp1.pt3.x == -1
        assert triangle_fp1.pt3.y == -8

        assert self.triangle_1 == triangle_fp1

        p1 = Point(-5.5, -10.255)
        p2 = Point(9, 8.34)
        p3 = Point(5, -17.9)
        
        triangle_fp2 = Triangle.from_points((p1, p2, p3))

        assert triangle_fp2.pt1.x == -5.5
        assert triangle_fp2.pt1.y == -10.255
        assert triangle_fp2.pt2.x == 9
        assert triangle_fp2.pt2.y == 8.34
        assert triangle_fp2.pt3.x == 5
        assert triangle_fp2.pt3.y == -17.9

        assert self.triangle_4 == triangle_fp2

        p1 = Point(-50, -25)
        p2 = Point(0, 37)
        p3 = Point(48, -13)
        
        triangle_fp3 = Triangle.from_points((p1, p2, p3))

        assert triangle_fp3.pt1.x == -50
        assert triangle_fp3.pt1.y == -25
        assert triangle_fp3.pt2.x == 0
        assert triangle_fp3.pt2.y == 37
        assert triangle_fp3.pt3.x == 48
        assert triangle_fp3.pt3.y == -13

        assert self.triangle_3 == triangle_fp3
    
    def test_str(self):
        assert str(self.triangle_1) == "[(4, 2), (1, 3), (-1, -8)]"
        assert str(self.triangle_2) == "[(5, 5), (-3, 2), (0, 0)]"
        assert str(self.triangle_3) == "[(-50, -25), (0, 37), (48, -13)]"
        assert str(self.triangle_4) == "[(-5.5, -10.255), (9, 8.34), (5, -17.9)]"
        assert str(self.triangle_5) == "[(-50, -25), (0, 37), (48, -13)]"

    def test_repr(self):
        assert repr(self.triangle_1) == "Triangle(4, 2, 1, 3, -1, -8)"
        assert repr(self.triangle_2) == "Triangle(5, 5, -3, 2, 0, 0)"
        assert repr(self.triangle_3) == "Triangle(-50, -25, 0, 37, 48, -13)"
        assert repr(self.triangle_4) == "Triangle(-5.5, -10.255, 9, 8.34, 5, -17.9)"
        assert repr(self.triangle_5) == "Triangle(-50, -25, 0, 37, 48, -13)"



    def test_ne(self):
        assert self.triangle_5 != self.triangle_1
        assert self.triangle_4 != Triangle(0, 0, 0, 0, 0, 0)
        assert self.triangle_2 != self.triangle_3

        assert not (self.triangle_2 != Triangle(5, 5, -3, 2, 0, 0))
        assert not (self.triangle_4 != self.triangle_4)
        assert not (self.triangle_5 != self.triangle_3)

        with pytest.raises(TypeError):
            self.triangle_3 != "xyz"

    
    def test_center(self):

        assert self.triangle_2.center == Point(0.66667, 2.33333)
        assert self.triangle_1.center == Point(1.33333, -1.0)
        assert self.triangle_4.center == Point(2.83333, -6.605)
        assert self.triangle_5.center == Point(-0.66667, -0.33333)

        assert self.triangle_3.center != Point(0, 0)
        assert self.triangle_4.center != Point(-1, -1)

    def test_area(self):
        
        assert pytest.approx(self.triangle_4.area(), 0.01) == 153.05
        assert pytest.approx(self.triangle_2.area(), 0.1) == 12.5

        assert pytest.approx(self.triangle_1.area(), 0.1) != 20.0
        assert self.triangle_3.area() != 4958392
        assert pytest.approx(self.triangle_4.area(), 0.01) != 100.0
        assert self.triangle_2.area() != 0

    def test_move(self):
        self.triangle_1.move(1, -1)
        assert self.triangle_1 == Triangle(5, 1, 2, 2, 0, -9)

        self.triangle_2.move(-2, 3)
        assert self.triangle_2 == Triangle(3, 8, -5, 5, -2, 3)

        self.triangle_3.move(10, 10)
        assert self.triangle_3 == Triangle(-40, -15, 10, 47, 58, -3)

        self.triangle_4.move(0, 0)
        assert self.triangle_4 == Triangle(-5.5, -10.255, 9, 8.34, 5, -17.9)

        self.triangle_5.move(-2.5, 4.75)
        assert self.triangle_5 == Triangle(-52.5, -20.25, -2.5, 41.75, 45.5, -8.25)



    def test_top(self):
        assert self.triangle_1.top == 3
        assert self.triangle_2.top == 5
        assert self.triangle_3.top == 37

        assert self.triangle_3.top != 0

    def test_bottom(self):
        assert self.triangle_4.bottom == -17.9
        assert self.triangle_5.bottom == -25
        assert self.triangle_1.bottom == -8

        assert self.triangle_5.top != 25

    def test_left(self):
        assert self.triangle_1.left == -1
        assert self.triangle_5.left == -50
        assert self.triangle_3.left == -50

        assert self.triangle_4.top != 12394859823423

    def test_right(self):
        assert self.triangle_2.right == 5
        assert self.triangle_1.right == 4
        assert self.triangle_4.right == 9

    def test_height(self):
        assert self.triangle_3.height == 62
        assert self.triangle_2.height == 5
        assert self.triangle_1.height == 11

    def test_width(self):
        assert self.triangle_3.width == 98
        assert self.triangle_4.width == 14.5
        assert self.triangle_5.width == 98

    def test_topleft(self):
        assert self.triangle_1.topleft == Point(-1, 3)
        assert self.triangle_2.topleft == Point(-3, 5)
        assert self.triangle_3.topleft == Point(-50, 37)

    def test_bottomright(self):
        assert self.triangle_2.bottomright == Point(5, 0)
        assert self.triangle_5.bottomright == Point(48, -25)
        assert self.triangle_1.bottomright == Point(4, -8)

    def test_bottomleft(self):
        assert self.triangle_3.bottomleft == Point(-50, -25)
        assert self.triangle_5.bottomleft == Point(-50, -25)
        assert self.triangle_1.bottomleft == Point(-1, -8)

    def test_topright(self):
        assert self.triangle_1.topright == Point(4, 3)
        assert self.triangle_2.topright == Point(5, 5)
        assert self.triangle_4.topright == Point(9, 8.34)

        assert self.triangle_4.topright != Point(0, 0)

    def test_bounding_box(self):

        assert self.triangle_1.bounding_box == (
            self.triangle_1.bottomleft,
            self.triangle_1.bottomright,
            self.triangle_1.topleft,
            self.triangle_1.topright)

        assert self.triangle_5.bounding_box == (
            self.triangle_5.bottomleft,
            self.triangle_5.bottomright,
            self.triangle_5.topleft,
            self.triangle_5.topright)

        assert self.triangle_3.bounding_box == (
            self.triangle_3.bottomleft,
            self.triangle_3.bottomright,
            self.triangle_3.topleft,
            self.triangle_3.topright)
