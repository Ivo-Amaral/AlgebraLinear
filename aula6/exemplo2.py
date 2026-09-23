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

print("u - v=", u - v)
print("v - u=", v - u)