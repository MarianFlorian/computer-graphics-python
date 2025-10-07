import matplotlib.pyplot as plt

# Setăm figura și axele
fig, ax = plt.subplots()
ax.set_title("Sistem de axe OXY cu 3 drepte")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Plasăm axele X și Y în centru
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Ascundem marginile de sus și dreapta
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Plasăm săgeți la capătul axelor
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Domeniu pentru desen
x = range(-10, 11)

# 1. Dreaptă verticală: x = 2
ax.axvline(x=2, color='red', label='Dreaptă verticală: x = 2')

# 2. Dreaptă orizontală: y = -1
ax.axhline(y=-1, color='green', label='Dreaptă orizontală: y = -1')

# 3. Dreaptă oblică: y = 2x + 1
y_oblica = [2*i + 1 for i in x]
ax.plot(x, y_oblica, color='blue', label='Dreaptă oblică: y = 2x + 1')

# Afișăm grilajul și legenda
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
ax.set_aspect('equal')

plt.show()
