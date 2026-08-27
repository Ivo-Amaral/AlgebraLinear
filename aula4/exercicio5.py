import numpy as np

u1 = int(input("Digite x1: "))
u2 = int(input("Digite x2: "))
v1 = int(input("Digite y1: "))
v2 = int(input("Digite y2: "))

u = np.array([u1, u2])
v = np.array([v1, v2])

produto = np.dot(u, v)                  # u. v
norma_v2 = np.dot(v, v)                 # ||v||^2

k = produto / norma_v2
proj = k * v

print("u * v = ", produto)
print("||v||^2 = ", norma_v2)
print("k = ", k)
print("proj = ", proj)