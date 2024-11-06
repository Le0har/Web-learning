import unittest
from quadratic_equation import solve_quadratic_equation
from decimal import Decimal


class TestQadraticEquation(unittest.TestCase):
    def test_no_roots(self):
        self.assertEqual(solve_quadratic_equation(1, 0, 1), [])                 # task test 1
        self.assertEqual(solve_quadratic_equation(1, -5, 9), [])
        self.assertEqual(solve_quadratic_equation(4, 0, 8), [])

    def test_one_root(self):
        self.assertEqual(solve_quadratic_equation(1, 2, 1), [-1])               # task test 3
        self.assertEqual(solve_quadratic_equation(1, 2, 0.99999975), [-1])      # task test 5
        self.assertEqual(solve_quadratic_equation(1, -12, 36), [6])
        self.assertEqual(solve_quadratic_equation(4, -12, 9), [1.5])
        self.assertEqual(solve_quadratic_equation(1, 1, 0.2500000003), [-0.5])  # D = -0.0000000012

    def test_two_roots(self):
        self.assertEqual(solve_quadratic_equation(1, 0, -1), [1, -1])           # task test 2
        self.assertEqual(solve_quadratic_equation(3, 11, 6), [Decimal('-0.666667'), -3])
        self.assertEqual(solve_quadratic_equation(1, 17, -18), [1, -18])  
        self.assertEqual(solve_quadratic_equation(-3, 0, 75), [-5, 5])
        self.assertEqual(solve_quadratic_equation(2, 4, 0), [0, -2])  

    def test_coefficient_a_equal_zero(self):
        with self.assertRaises(ValueError):
            solve_quadratic_equation(0, 4, 5)                                   # task test 4
        with self.assertRaises(ValueError):
            solve_quadratic_equation(-0.0000000012, 4, 5)                       # a = -0.0000000012           


if __name__ == '__main__':
    unittest.main()