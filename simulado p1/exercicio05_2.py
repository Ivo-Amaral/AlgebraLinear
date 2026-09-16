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

# b) Módulo de v ao quadrado
modulo_v_quadrado = vx**2 + vy**2

# Coeficiente k
k = produto / modulo_v_quadrado

# c) Projeção de u sobre v
projecao = k * v

print("\nProduto escalar:", produto)
print("||v||²:", modulo_v_quadrado)
print("Coeficiente k:", k)
print("Projeção:", projecao)