import numpy as np

print("Digite o vetor u:")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("\nDigite o vetor v:")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

u = np.array([ux, uy])
v = np.array([vx, vy])

# a) Produto escalar
produto = np.dot(u, v)

print("\nProduto escalar:", produto)

# b) Verificar se são ortogonais
if produto == 0:
    # c) Resultado
    print("Os vetores são ortogonais.")
    print("Os vetores formam um ângulo de 90°.")
else:
    print("Os vetores não são ortogonais.")