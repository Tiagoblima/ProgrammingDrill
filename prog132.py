import math
import matplotlib.pyplot as plt

print("Type de component: ")

u = float(input("Type U value: "))
v = float(input("Type V value: "))

print("Type de complex number")

a = float(input("a: "))
b = float(input("b: "))

plt.quiver([0, 0], [0, 0], [u, u * a], [v, v * b], angles='xy', scale_units='xy', scale=1)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
