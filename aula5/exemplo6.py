import numpy as np

print("Digite o vetor u: ")
ux = float(input("u(x): "))
uy = float(input("u(y): "))

print("Digite o vetor v: ")
vx = float(input("v(x): "))
vy = float(input("v(y): "))

print("Digite o vetor w: ")
wx = float(input("w(x): "))
wy = float(input("w(y): "))

u = np.array([ux, uy])
v = np.array([vx, vy])
w = np.array([wx, wy])

A = np.column_stack((u, v))

det = np.linalg.det(A)
print("Determinante de A =", det)

if not np.isclose(det, 0):
    a, b = np.linalg.solve(A, w)
    resultado = a * u + b * v

    print("Destino atingivel com soluções única.")
    print("a =", a)
    print("b =", b)
    print("Verificação =", resultado)

else:
    print("Os vetores u e v são lineamente dependentes.")
    print("Não existe uma solução unica para os coeficientes.")