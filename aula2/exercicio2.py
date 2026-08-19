import numpy as np
import matplotlib.pyplot as plt

A = np.array([2,1])
B = np.array([8,7])
C = np.array([12,4])

AB = B - A
BC = C - B

dist_AB = np.linalg.norm(AB)
dist_BC = np.linalg.norm(BC)

cos_theta = np.dot(AB, BC) / (dist_AB * dist_BC)
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)

plt.figure(figsize=(8, 6))
plt.plot([A[0], B[0], C[0]], [A[1], B[1], C[1]], 'bo-', label='Trajetória')

plt.quiver(A[0], A[1], AB[0], AB[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vetor AB')
plt.quiver(B[0], B[1], BC[0], BC[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vetor BC')

plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')

plt.title(f"Deslocamento do Drone\nDist AB: {dist_AB:.2f}, Dist BC: {dist_BC:.2f}, Ângulo: {angle_deg:.2f}°")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()