import unittest

def add_poly(poly1, poly2):
    result = []
    res_len = max(len(poly1), len(poly2))

    for i in range(res_len):
        helper1 = 0
        helper2 = 0

        if i < len(poly1):
            helper1 = poly1[i]
        if i < len(poly2):
            helper2 = poly2[i]

        result.append(helper1 + helper2)
    return result


def sub_poly(poly1, poly2):
    res_len = max(len(poly1), len(poly2))
    result = []

    for i in range(res_len):
        helper = 0
        if i < len(poly1):
            helper += poly1[i]
        if i < len(poly2):
            helper -= poly2[i]

        result.append(helper)
    return result


def mul_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]
    
    return result

def is_zero(poly):
    for element in poly:
        if element != 0:
            return False
    return True

def eq_poly(poly1, poly2):
    return poly1 == poly2

def eval_poly(poly, x0):
    result = 0
    x_pow = 1 
    for element in poly:
        result += element * x_pow 
        x_pow *= x0 
    return result

def combine_poly(poly1, poly2):
    result = [poly1[-1]]
    for element in reversed(poly1[:-1]):
        result = add_poly(mul_poly(result, poly2), [element])

    return result


def pow_poly(poly, n):
    result = [1]
    for i in range(n):
        result = mul_poly(result, poly)
    return result


def diff_poly(poly):
    result = []
    for i in range(1, len(poly)): #od 1 bo pierwszy wyraz wolny zawsze stanie sie zerem
        result.append(poly[i] * i)
    return result


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]
        self.p2 = [0, 0, 1]
        self.p3 = [1, 2]
        self.p4 = [1, 0, 1]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p4, self.p2), [1, 0, 0])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p2, self.p4), [0, 0, 1, 0, 1])

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 0, 0, 0, 0]))  
        self.assertFalse(is_zero([5, 0, 1])) 

    def test_eq_poly(self):
        self.assertTrue(eq_poly(self.p3, [1, 2]))
        self.assertFalse(eq_poly(self.p1, self.p2))

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p2, 4), 16)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p3, self.p2), [1, 0, 2])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p4, 2), [1, 0, 2, 0, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p3), [2])

    def tearDown(self):
        self.p1 = [] 
        self.p2 = [] 
        self.p3 = [] 
        self.p4 = []

if __name__ == '__main__':
    unittest.main() 
