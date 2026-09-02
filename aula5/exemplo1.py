import numpy as np
u = np.array([2,1])
v = np.array([1,3])
w = np.array([5,7])

A = np.column_stack((u,v))
a, b = np.linalg.solve(A, w)

print("a =", a)
print("b =", b)
print("Verificação =", a*u + b*v)