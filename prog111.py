import math

print("Type the first complex number")

a1 = float(input("a: "))
b1 = float(input("b: "))

print("Type the second complex numeber")

a2 = float(input("a: "))
b2 = float(input("b: "))


print("c1: {0} + {1}i\nc2: {2} + {3}i".format(a1,b1,a2,b2))

sumA = a1 + a2

sumB = b1 + b2

print("Sum of c1 and c2: {0} + {1}i".format(sumA, sumB))

mulA = a1 * a2 - b1 * b2
mulB = a2 * b1 + a1 * b2

print("Multiplication of c1 and c2: {0} + {1}i".format(mulA, mulB))

subA = a1 - a2
subB = b1 - b2


#Programing Drill 1.2.1
print("Subtraction of c1 and c2: {0} + {1}i".format(subA, subB))

modulusC1 = math.sqrt(pow(a1,2) + pow(b1, 2))
modulusC2 = math.sqrt(pow(a2, 2) + pow(b2, 2))

try:

 divX = (a1 * a2 + b1 * b2)/modulusC2
 divY = (a2 * b1 - a1 * b2)/modulusC2
 print("Division of c1 and c2: {0} + {1}i".format(divX, divY))

except(ZeroDivisionError, NameError):
    print("Zero Division Error")

print("Modulus c1: {0}\nModulus c2 {1}".format(modulusC1, modulusC2))
b1 *= -1
b2 *= -1
if b1 > 0:
    msg = "Conjugado c1: {0} + {1}i"
else:
    msg = "Conjugado c1: {0} {1}i"


print(msg.format(a1, b1))

if b2 > 0:
    msg = "Conjugado c2: {0} + {1}i"
else:
    msg = "Conjugado c2: {0} {1}i"

print(msg.format(a2, b2))
