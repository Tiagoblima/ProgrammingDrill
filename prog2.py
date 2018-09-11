from complex_vector import *

u, v, w = [], [], []
try:
    n = int(input("Type the vector size: "))
    u = vector_input(n)
    v = vector_input(3)
    w = add_vector(u, v)

    print("u: ", u, "\nv: ", v, "\nw: ", w)
except ValueError:
    print("ERROR: Vector's size must be a integer")
except LengthError:
    print("ERROR: The length of the vector must be the same")

a = [[]]
try:
    n = int(input("Type the n: "))
    m = int(input("Type the m: "))
    a = matrix_input(n, m)
    print(a)
except ValueError:
    print("ERROR: Matrix's size must be integer")


