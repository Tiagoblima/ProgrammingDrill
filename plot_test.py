import math
import matplotlib.pyplot as plt
from complex_number import *

plt.xlim(-10, 10)
plt.ylim(-10, 10)

w = (-2, -1)

c1 = (1, 1)
c2 = (1, 0)

u = [1]
v = [1]

i = 0

originX = [0]
originY = [0]

while i < 2:
    originX.append(0)
    originY.append(0)
    c3 = sum(c1, c2)
    u.append(c3[0])
    v.append(c3[1])
    c1 = c3
    i += 1

plt.quiver(originX, originY, u, v, angles='xy', scale_units='xy', scale=1)

plt.show()
