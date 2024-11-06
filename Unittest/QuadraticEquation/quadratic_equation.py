import math


def solve_quadratic_equation(a, b, c):      # ax^2 + bx + c = 0
    if math.isclose(a, 0):
        raise ValueError('The coefficient "a" cannot be equal to zero')
    roots_equation = []
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return roots_equation
    elif math.isclose(discriminant, 0, abs_tol=0.00001):
        x = -b / (2 * a)
        roots_equation.append(x)
        return roots_equation
    elif discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a) 
        roots_equation.extend([x1, x2])
        return roots_equation

