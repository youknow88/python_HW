
import math

variable_a = 5
variable_b = 2
variable_c = 10
varieble_d = variable_a + variable_b * (variable_c / 2)
print ("Переменная d, при значении переменной a - %d, переменной b - %d и пременной с - %d равна %d"
%( variable_a , variable_b , variable_c , varieble_d))

var_a = 4
var_b = 2
var_c = (var_a**2 + var_b**2) % 2
print ( "При значении переменной a - %d, переменной b - %d, переменная c равна %d" % (var_a , var_b , var_c  ))

variab_a = 40
variab_b = 120
variab_c = 200
variab_d =  ( variab_a + variab_b) / 12 * variab_c % 4 + variab_b
print ("При значении переменной a - %d, переменной b  - %d и переменной с - %d, переменная d равна %.2f"
% ( variab_a , variab_b ,variab_c , variab_d ))

vari_a = 200
vari_b = 30
vari_c = 6
vari_d = (vari_a - vari_b * vari_c) / ( vari_a + vari_b) % vari_c
print ("При значении переменной a - %d, переменной b - %d и переменной с - %d, переменная d равна %.2f"
% ( vari_a , vari_b , vari_c , vari_d  ))

var_a1 = 37
var_b1 = 80
var_c1 = 90
var_d1 = math.fabs( var_a1 - var_b1) / ( var_a1 + var_b1) ** 3 - math.cos (var_c1)
print ("При значении переменной a1 - %d, переменной b1 - %d и переменной c1 - %d, переменная d1 равна %.2f"
% ( var_a1 , var_b1 , var_c1 , var_d1) )

var_a2 = 55
var_b2 = 73
var_c2 = 42
var_d2 = (math.log1p (1 + var_c2) - var_b2)**4 + math.fabs (var_a2)
print ( "При значении переменной a2 - %d, переменной b2 - %d и переменной с2 - %d, переменная d равна %.2f "
% ( var_a2 , var_b2 , var_c2 , var_d2 ))