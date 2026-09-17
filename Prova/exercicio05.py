import numpy as np

print("Digite o vetor u:")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("\nDigite o vetor v:")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

u = np.array([ux, uy])
v = np.array([vx, vy])

produto = np.dot(u, v)

modulo_v = np.linalg.norm(v)
modulo_v_quadrado = modulo_v ** 2

k = produto / modulo_v_quadrado

projecao = k * v

print("\nProduto escalar u.v:", produto)
print("||v||²:", modulo_v_quadrado)
print("Coeficiente k:", k)
print("Projeção de u sobre v:", projecao)