import numpy as np

u1 = int(input("Digite x1: "))
u2 = int(input("Digite x2: "))
v1 = int(input("Digite y1: "))
v2 = int(input("Digite y2: "))

u = np.array([u1, u2])
v = np.array([v1, v2])

uv = v-u

dot_product = np.linalg.norm(uv)
print("Produto escalar de u e v = ", dot_product)