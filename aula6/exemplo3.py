import numpy as np

u = np.array([
    float(input("Digite o valor de ux: ")),
    float(input("Digite o valor de uy: ")),
    float(input("Digite o valor de uz: "))
])

k = float(input("Digite o valor de k: "))

resultado = k * u

print("u =", u)
print("k =", k)
print("k * u =", resultado)