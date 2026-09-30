import numpy as np

produto = 0.00000001

if np.isclose(produto, 0):
    print("Os vetores são ortogonais.")
else:
    print("Os vetores não são ortogonais.")