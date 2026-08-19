import numpy as np
from matplotlib import pyplot as plt

a = np.array([3, 9])

print(np.linalg.norm(a))

plt.quiver(0, 0, 3, 9, angles="xy", scale_units="xy", scale=1)
plt.xlim(0, 4)
plt.ylim(0, 10)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()