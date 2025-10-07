import matplotlib.pyplot as plt

def bresenham(x0, y0, x1, y1):
    """Algoritmul de rasterizare al lui Bresenham între două puncte (x0,y0) și (x1,y1)"""
    puncte = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            puncte.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            puncte.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    puncte.append((x1, y1))
    return puncte

# Exemplu
x_start, y_start = 2, 2
x_end, y_end = 12, 7
linie = bresenham(x_start, y_start, x_end, y_end)


x_vals, y_vals = zip(*linie)
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y_vals, marker='s', color='black', linestyle='None', markersize=10)
plt.grid(True)
plt.gca().invert_yaxis()  # Ca în ecranele grafice, y crește în jos
plt.title("Algoritmul de Bresenham - Linie între două puncte")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.show()
