#Um robô movimenta-se no plano R² passando pelos pontos A, B e C. Desenvolva um programa 
#em Python que permita ao operador informar as coordenadas dos três pontos. Capture, 
#utilizando input(), os valores x e y dos pontos A, B e C.
#a) Calcule os vetores de deslocamento AB = B - A e BC = C - B.
#b) Calcule as distâncias ||AB|| e ||BC||.
#c) Apresente os vetores calculados e a distância total percorrida pelo robô.
#Valores sugeridos apenas para teste: A = (1, 2), B = (5, 5), C = (8, 9).


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

# Criando os pontos
A = np.array([ax, ay])
B = np.array([bx, by])
C = np.array([cx, cy])

# a) Vetores de deslocamento
AB = B - A
BC = C - B

# b) Distâncias
distancia_AB = np.linalg.norm(AB)
distancia_BC = np.linalg.norm(BC)

# c) Distância total
distancia_total = distancia_AB + distancia_BC

print("\nVetor AB:", AB)
print("Vetor BC:", BC)

print("Distância AB:", distancia_AB)
print("Distância BC:", distancia_BC)

print("Distância total percorrida:", distancia_total)