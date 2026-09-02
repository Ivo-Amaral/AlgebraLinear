import numpy as np

u = np.array([1,4])
v = np.array([2, -1])
w = np.array([7, 3])

A = np.column_stack((u,v))
a, b = np.linalg.solve(A, w)

print("a =", a)
print("b =", b)
print("Verificação =", a*u + b*v)