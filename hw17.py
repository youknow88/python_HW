import math

def solve_quadratic_equation(a, b, c):
    d = b**2 - 4 * a * c
    if a != 0:
        if d < 0:
            return None, None
        if d > 0:
            root1 = (-b + math.sqrt(d)) / (2 * a)
            root2 = (-b - math.sqrt(d)) / (2 * a)
            return root1, root2
        if d == 0:
            root = -b / 2 * a
            return root, None

print(solve_quadratic_equation(1, 2, 1))