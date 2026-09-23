import numpy as np

v = np.array([
    float(input("Digite o valor de vx: ")),
    float(input("Digite o valor de vy: ")),
    float(input("Digite o valor de vz: "))
])

modulo = np.linalg.norm(v)

print("v= ", v)
print("||v||= ", modulo)