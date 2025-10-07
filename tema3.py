import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def rotatie_z(punct, unghi_gr):

    theta = np.radians(unghi_gr)
    matrice_rotatie = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0,              0,             1]
    ])
    return matrice_rotatie @ punct


puncte = np.array([
    [1, 1, 0],
    [1, -1, 0],
    [-1, -1, 0],
    [-1, 1, 0],
    [1, 1, 2],
    [1, -1, 2],
    [-1, -1, 2],
    [-1, 1, 2]
])


unghi = 45
puncte_rotate = np.array([rotatie_z(p, unghi) for p in puncte])


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(puncte[:, 0], puncte[:, 1], puncte[:, 2], color='red', label='Inițial')

ax.scatter(puncte_rotate[:, 0], puncte_rotate[:, 1], puncte_rotate[:, 2], color='blue', label=f'Rotit cu {unghi}°')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Rotație 3D în jurul axei Z")
ax.legend()
plt.show()
