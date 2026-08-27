import numpy as np

u1 = int(input("Digite x1: "))
u2 = int(input("Digite x2: "))
v1 = int(input("Digite y1: "))
v2 = int(input("Digite y2: "))

u = np.array([u1, u2])
v = np.array([v1, v2])

s = u+v

print("vetor u+v = ", s)