import numpy as np

x = float(input("Digite o valor de x: "))
y = float(input("Diite o valor de y: "))

sx = float(input("Digite o valor de sx: "))
sy = float(input("Diite o valor de sy: "))

A = np.array([[sx, 0], [0, sy]], dtype=float)
v = np.array([x, y], dtype=float)

c = A @ v

print(f"T({v})={c}")