import numpy as np
import matplotlib.pyplot as plt

A = np.array([0,0])
B = np.array([6,8])
C = np.array([10,3])

AB = B - A
BC = C - B

dist_AB = np.linalg.norm(AB)
dist_BC = np.linalg.norm(BC)