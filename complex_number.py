import math
import matplotlib.pyplot as plt


# Programming Drill 1.1.1

def sum(c1, c2):
    result = c1[0] + c2[0], c1[1] + c2[1]
    return result


# Programming Drill 1.2.1

def sub(c1, c2):
    result = c1[0] - c2[0], c1[1] - c2[1]
    return result


def mult(c1, c2):
    result = c1[0] * c2[0] - c1[1] * c2[1], c2[0] * c1[1] + c1[0] * c2[1]
    return result


def modulus(c):
    mod = math.sqrt(pow(c[0], 2) + pow(c[1], 2))
    return round(mod)


def division(c1, c2):
    try:

        x = (c1[0] * c2[0] + c1[1] * c2[1]) / modulus(c2)
        y = (c2[0] * c1[1] - c1[0] * c2[1]) / modulus(c2)

        result = round(x), round(y)
        return result
    except(ZeroDivisionError, NameError):
        print("Zero Division Error or NameError")


def conjugate(c):
    conj = c[0], c[1] * -1
    return conj


####################################

# Programming Drill 1.3.1

def to_polar(c):
    p = modulus(c)
    o = math.atan(c[1] / c[0])

    polar = p, round(o)
    return polar


def to_cartesian(polar):
    a = round(polar[0] * math.cos(polar[1]))
    b = round(polar[0] * math.sin(polar[1]))

    result = (a, b)
    return result


###############################

# Programming Drill 1.3.3

def polar_mul(polar1, polar2):
    p = polar1[0] * polar2[0]
    o = polar1[1] + polar2[1]

    result = p, o
    return result


def polar_div(polar1, polar2):
    p = polar1[0] / polar2[0]
    o = polar1[1] - polar2[1]

    result = round(p), o
    return result


def Draw(u, v):
    plt.quiver(u, v, angles='xy', scale_units='xy', scale=1)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()


def op_input():
    n = int(input("Type the vector size: "))

    i = 0
    u = []
    while i < n:
        print("First vector: ")
        str = input("format: (a,b):")
        str = str.split(",")
        a = int(str[0])
        b = int(str[1])
        c = (a, b)
        u.append(c)
        i += 1
    print(u)

