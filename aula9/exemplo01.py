import numpy as np

x= float(input("Digite o valor de x: "))
y= float(input("Digite o valor de y: "))
k= float(input("Digite o valor de k: "))

v = np.array([x, y])

A = np.array([
    [k, 0],
    [0, k]
])

resultado = A @ v

print("Vetor original de v: ", v)
print("Matriz de escala:")
print(A)
print("T(v) = ", resultado)