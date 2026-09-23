import numpy as np

u = np.array([
    float(input("Digite o valor de ux: ")),
    float(input("Digite o valor de uy: ")),
    float(input("Digite o valor de uz: "))
])

v = np.array([
    float(input("Digite o valor de vx: ")),
    float(input("Digite o valor de vy: ")),
    float(input("Digite o valor de vz: "))
])

produto = np.dot(u, v)

print("u.v=", produto)

if np.isclose(produto, 0):
    print("Os vetores são ortogonais.")
else:
    print("Os vetores não são ortogonais.")