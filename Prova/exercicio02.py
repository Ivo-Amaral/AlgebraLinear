import numpy as np
import matplotlib.pyplot as plt

print("Digite o vetor u:")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("\nDigite o vetor v:")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

print("\nDigite o vetor w:")
wx = float(input("w(x): "))
wy = float(input("w(y): "))

u = np.array([ux, uy])
v = np.array([vx, vy])
w = np.array([wx, wy])

A = np.column_stack((u, v))

print("\nMatriz A:")
print(A)

coeficientes = np.linalg.solve(A, w)

a = coeficientes[0]
b = coeficientes[1]

print("\na =", a)
print("b =", b)

resultado = a * u + b * v

print("\na*u + b*v =", resultado)
print("w =", w)

if np.allclose(resultado, w):
    print("\nVerificação correta: a*u + b*v = w")
else:
    print("\nA verificação não foi satisfeita.")