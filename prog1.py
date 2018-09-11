import math
from complex_number import *

print("Type the first complex number")

str1 = input("format a,b: ")
str1 = str1.split(",")

print("Type the second complex numeber")

str2 = input("format a,b: ")
str2 = str2.split(",")

c1 = int(str1[0]), int(str1[1])
c2 = int(str2[0]), int(str2[1])

print("c1: {0} + {1}i\nc2: {2} + {3}i".format(c1[0], c1[1], c2[0], c2[1]))


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

plt.plot([2, 4, 6], [2, 4, 6])
plt.show()
Draw(c1, c2)


