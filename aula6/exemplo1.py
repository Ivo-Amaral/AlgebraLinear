import numpy as np

ux = float(input("Digite o valor de ux: "))
uy = float(input("Digite o valor de uy: "))
uz = float(input("Digite o valor de uz: "))

vx = float(input("Digite o valor de vx: "))
vy = float(input("Digite o valor de vy: "))
vz = float(input("Digite o valor de vz: "))

u = np.array([ux, uy, uz])
v = np.array([vx, vy, vz])

resultado = u + v

print("O valor de u é = ", u)
print("O valor de v é = ", v)
print("O resultado da soma de u + v é = ", resultado)