import numpy as np

print("Digite as coordenadas do ponto A:")
ax = float(input("A(x): "))
ay = float(input("A(y): "))

print("\nDigite as coordenadas do ponto B:")
bx = float(input("B(x): "))
by = float(input("B(y): "))

print("\nDigite as coordenadas do ponto C:")
cx = float(input("C(x): "))
cy = float(input("C(y): "))

A = np.array([ax, ay])
B = np.array([bx, by])
C = np.array([cx, cy])

AB = B - A
BC = C - B

distancia_AB = np.linalg.norm(AB)
distancia_BC = np.linalg.norm(BC)

distancia_total = distancia_AB + distancia_BC

print("\nVetor AB:", AB)
print("Vetor BC:", BC)

print("Distância AB:", distancia_AB)
print("Distância BC:", distancia_BC)

print("Distância total percorrida:", distancia_total)