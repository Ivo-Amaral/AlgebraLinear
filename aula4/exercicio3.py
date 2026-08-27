import numpy as np

f1 = int(input("Digite x1: "))
f2 = int(input("Digite x2: "))
escalar = int(input("Digite o escalar: "))
f = np.array([f1, f2])
result = escalar * f
print("vetor f multiplicado pelo escalar = ", result)