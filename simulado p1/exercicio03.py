import numpy as np

print("Digite o vetor u:")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("\nDigite o vetor v:")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

k = float(input("\nDigite o valor de k: "))

u = np.array([ux, uy])
v = np.array([vx, vy])

# a) Produto escalar
produto = np.dot(u, v)

# b) Módulos
modulo_u = np.linalg.norm(u)
modulo_v = np.linalg.norm(v)

# c) Multiplicação pelo escalar
ku = k * u
kv = k * v

print("\nProduto escalar:", produto)

print("Módulo de u:", modulo_u)
print("Módulo de v:", modulo_v)

print("k * u:", ku)
print("k * v:", kv)