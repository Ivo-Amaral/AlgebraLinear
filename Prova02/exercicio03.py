import numpy as np

a11 = float(input("Coeficiente de x (linha 1): "))
a12 = float(input("Coeficiente de y (linha 1): "))
b1 = float(input("termo independente (linha 1): "))

a21 = float(input("Coeficiente de x (linha 2): "))
a22 = float(input("Coeficiente de y (linha 2): "))
b2 = float(input("termo independente (linha 2): "))

A = np.array([[a11, a12], [a21, a22]], dtype=float)
b = np.array([b1, b2], dtype=float)

solucao = np.linalg.solve(A, b)
print(f"x = R${solucao[0]:.2f}")
print(f"y = R${solucao[1]:.2f}")