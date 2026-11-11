import numpy as np

print("Digite os dados da matriz A (2x2): ")
A = np.array([
    [float(input("A[1,1]: ")), float(input("A[1,2]: "))],
    [float(input("A[1,1]: ")), float(input("A[1,2]: "))]
])

print("\nDigite os dados da matriz B (2x2): ")
B = np.array([
    [float(input("B[1,1]: ")), float(input("B[1,2]: "))],
    [float(input("B[1,1]: ")), float(input("B[1,2]: "))]
])

k = float(input("\nDigite o valor do escalar k: "))

soma = A + B
escalar = k * A

print("\nA + B = \n", soma)
print("kA =\n", escalar)

if A.shape[1] == B.shape[0]:
    AB = A @ B
    print("A * B=\n", AB)
else:
    AB = B @ A
    print("A * B não pode ser calculado.")

if B.shape[1] == A.shape[0]:
    BA = B @ A
    print("B * A =\n", BA)
else:
    AB = B @ A
    print("B * A não pode ser calculado.")

if AB is not None and BA is not None:
    if np.array_equal(AB,BA):
        print("Neste caso, A*B = B*A.")
    else:
        print("Neste caso, A*B <> B*A.")