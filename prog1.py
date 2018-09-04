import math
from complex_number import *

print("Type the first complex number")

a1 = float(input("a: "))
b1: float = float(input("b: "))

print("Type the second complex numeber")

a2 = float(input("a: "))
b2 = float(input("b: "))

print("c1: {0} + {1}i\nc2: {2} + {3}i".format(a1, b1, a2, b2))

c1 = a1, b1
c2 = a2, b2

sum = sum(c1, c2)
print("Sum of c1 and c2: {0}".format(sum))

mul = mult(c1, c2)
print("Multiplication of c1 and c2: {0}".format(mul))

sub = sub(c1, c2)
print("Subtraction of c1 and c2: {0}".format(sub))

div = division(c1, c2)
print("Division of c1 and c2: {0}".format(div))

print("Modulus c1: {0}\nModulus c2 {1}".format(modulus(c1), modulus(c2)))

print("Conjugado c1: {0} c2: {1}".format(conjugate(c1), conjugate(c2)))


polar1 = to_polar(c1)
polar2 = to_polar(c2)
print("Polar Representations c1: {0} c2: {1}".format(polar1, polar2))
print("Cartesian Representation c1: {0} c2: {1}".format(to_cartesian(polar1), to_cartesian(polar2)))

print("Polar Division: {0}".format(polar_div(polar1, polar2)))
print("Polar Multiplication {0}".format(polar_mul(polar1, polar2)))


Draw(c1, c2)
