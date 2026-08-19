from matplotlib import pyplot as plt

plt.quiver(0, 0, 4, 2, angles="xy", scale_units="xy", scale=1)
plt.xlim(0, 5)
plt.ylim(0, 4)
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

import numpy as np
v = np.array([2,3,5])
print('Módulo do vetor: ', np.linalg.norm(v))