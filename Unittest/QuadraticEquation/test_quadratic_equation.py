import unittest
import quadratic_equation


class TestQadraticEquation(unittest.TestCase):
    def test_no_roots(self):
        self.assertEqual(quadratic_equation.solve_quadratic_equation(1, 0, 1), [])               # task test 1
        self.assertEqual(quadratic_equation.solve_quadratic_equation(1, -5, 9), [])
        self.assertEqual(quadratic_equation.solve_quadratic_equation(4, 0, 8), [])

    def test_one_root(self):
        self.assertEqual(quadratic_equation.solve_quadratic_equation(1, 2, 1), [-1])            # task test 3
        self.assertEqual(quadratic_equation.solve_quadratic_equation(1, 2, 0.99999975), [-1])   # task test 5
        self.assertEqual(quadratic_equation.solve_quadratic_equation(1, -12, 36), [6])
        self.assertEqual(quadratic_equation.solve_quadratic_equation(4, -12, 9), [1.5])

    def test_two_roots(self):
        self.assertEqual(quadratic_equation.solve_quadratic_equation(1, 0, -1), [1, -1])        # task test 2
        self.assertEqual(quadratic_equation.solve_quadratic_equation(3, 11, 6), [-0.6666666666666666, -3])
        self.assertEqual(quadratic_equation.solve_quadratic_equation(1, 17, -18), [1, -18])  
        self.assertEqual(quadratic_equation.solve_quadratic_equation(-3, 0, 75), [-5, 5])
        self.assertEqual(quadratic_equation.solve_quadratic_equation(2, 4, 0), [0, -2])  

    def coefficient_a_equal_zero(self):
        with self.assertRaises(ValueError):
            quadratic_equation.solve_quadratic_equation(0, 4, 5)                                # task test 4


if __name__ == '__main__':
    unittest.main()