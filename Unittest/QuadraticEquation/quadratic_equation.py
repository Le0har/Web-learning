from decimal import Decimal, getcontext


def solve_quadratic_equation(a, b, c):      # ax^2 + bx + c = 0
    epsilon = 6
    getcontext().prec = epsilon
    a = Decimal(a)
    b = Decimal(b)
    c = Decimal(c)
    if a.quantize(Decimal('1.00000')) == 0:
        raise ValueError('The coefficient "a" cannot be equal to zero')
    roots_equation = []
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return roots_equation
    elif discriminant == 0:
        x = -b / (2 * a)
        roots_equation.append(x)
        return roots_equation
    elif discriminant > 0:
        x1 = (-b + discriminant.sqrt()) / (2 * a)
        x2 = (-b - discriminant.sqrt()) / (2 * a) 
        roots_equation.extend([x1, x2])
        return roots_equation

