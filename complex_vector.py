from complex_number import *


class LengthError(Exception): pass


def vector_input(n):
    print("format: a,b:")
    i = 0
    u = []
    while i < n:
        value = input("")
        value = value.split(",")
        a = float(value[0])
        b = float(value[1])
        c = (a, b)
        u.append(c)
        i += 1
    return u


def matrix_input(m, n):
    j = 0
    a = [[]]

    while j < m:
        print("vector {0}: ".format(j), end="")
        u = vector_input(n)
        a.append(u)
        j += 1
    a.pop(0)
    return a


def add_vector(u, v):
    w = []
    if len(u) != len(v):
        raise LengthError

    for i in range(len(u)):
        el = sum(u[i], v[i])
        w.append(el)

    return w
