import numpy as np
import matplotlib.pyplot as plt

print("Digite o vetor u:")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("\nDigite o vetor v:")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

print("\nDigite o vetor w:")
wx = float(input("w(x): "))
wy = float(input("w(y): "))

# Criando os vetores
u = np.array([ux, uy])
v = np.array([vx, vy])
w = np.array([wx, wy])

# a) Montando a matriz com u e v
A = np.column_stack((u, v))

print("\nMatriz A:")
print(A)

# Mostrar a matriz com Matplotlib
plt.figure(figsize=(4, 2))

plt.table(
    cellText=A,
    colLabels=["u", "v"],
    loc="center",
    cellLoc="center"
)

plt.axis("off")
plt.title("Matriz formada pelos vetores u e v")
plt.show()

# b) Encontrando os coeficientes a e b
coeficientes = np.linalg.solve(A, w)

a = coeficientes[0]
b = coeficientes[1]

print("\na =", a)
print("b =", b)

# c) Verificação
resultado = a * u + b * v

print("\na*u + b*v =", resultado)
print("w =", w)

if np.allclose(resultado, w):
    print("\nVerificação correta: a*u + b*v = w")
else:
    print("\nA verificação não foi satisfeita.")