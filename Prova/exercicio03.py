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

produto = np.dot(u, v)

modulo_u = np.linalg.norm(u)
modulo_v = np.linalg.norm(v)

ku = k * u
kv = k * v

print("\nProduto escalar:", produto)

print("||u||:", modulo_u)
print("||v||:", modulo_v)

print("k * u:", ku)
print("k * v:", kv)