import numpy as np

a11 = float(input("Digite o valor de a11: "))
a12 = float(input("Digite o valor de a12: "))
a21 = float(input("Digite o valor de a21: "))
a22 = float(input("Digite o valor de a22: "))

b11 = float(input("Digite o valor de b11: "))
b12 = float(input("Digite o valor de b12: "))
b21 = float(input("Digite o valor de b21: "))
b22 = float(input("Digite o valor de b22: "))

A = np.array([[a11, a12], [a21, a22]], dtype=float)
B = np.array([[b11, b12], [b21, b22]], dtype=float)

C = A + B

print("Estoque final: ", C)

k = float(input("Digite o valor de k: "))

escalar = k * C

print("Meta de estoque: ", escalar)