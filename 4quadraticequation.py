# Quadratic equation

import cmath
a = float(input("enter value of a : "))
b = float(input("enter value of a : "))
c = float(input("enter value of a : "))

print(a,b,c)
det = (b**2)- 4*a*c

sol1 = (-b-cmath.sqrt(det)/(2*a))
sol2 = (-b+cmath.sqrt(det)/(2*a))

print('the solution are {0} and {1}'. format(sol1,sol2))