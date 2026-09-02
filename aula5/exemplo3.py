import numpy as np

u = np.array([2, 3])
v = np.array([1, -1])
w = np.array([7, 4])

A = np.column_stack((u, v))
a, b = np.linalg.solve(A, w)

resultado = a * u + b * v

print("a =", a)
print("b =", b)
print("Verificação =", resultado)