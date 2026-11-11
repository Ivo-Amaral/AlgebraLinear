import numpy as np

print("digite os dados da Matriz A (2x2):")
A = np.array([
    [float(input("A[1,1]: ")), float(input("A[1,2]: "))],
    [float(input("A[2,1]: ")), float(input("A[2,2]: "))]
])

print("\nDigite os dados da Matriz B (2x2):")
B = np.array([
    [float(input("B[1,1]: ")), float(input("B[1,2]: "))],
    [float(input("B[2,1]: ")), float(input("B[2,2]: "))]
])

C = A + B

print("\nA = \n", A)
print("B = \n", B)
print("Dimensão de A: ", A.shape)
print("Dimensão de B: ", B.shape)
print("Total recebido (A + B) = \n", C)