import math

def triangle_square_and_perimeter(cathetus1, cathetus2):
   triangle_square = (cathetus1 * cathetus2) / 2
   triangle_perimeter =  math.sqrt(cathetus1 ** 2 + cathetus2 **2) + cathetus1 + cathetus2
   return triangle_square, triangle_perimeter

triangle_square, triangle_perimeter = triangle_square_and_perimeter( 10, 44)
print('Площадь прямоугольного треугольника = %.2fсм, а его периметр = %.2fсм'%(triangle_square, triangle_perimeter))


