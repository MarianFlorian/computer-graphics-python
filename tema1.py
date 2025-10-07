def aitken_neville(x_values, y_values, x):

    n = len(x_values)
    P = [[0.0 for _ in range(n)] for _ in range(n)]


    for i in range(n):
        P[i][i] = y_values[i]


    for j in range(1, n):
        for i in range(j, n):
            xi, xj = x_values[i - j], x_values[i]
            Pi_jm1 = P[i - 1][j - 1]
            Pi1_j = P[i][j - 1]
            P[i][j] = ((x - xi) * Pi1_j - (x - xj) * Pi_jm1) / (xj - xi)

    return P[n - 1][n - 1]

x_vals = [1.0, 1.3, 1.6, 1.9]
f_vals = [0.7652, 0.6201, 0.4554, 0.2818]

x_interp = 1.5

rezultat = aitken_neville(x_vals, f_vals, x_interp)
print(f"Valoarea interpolată a funcției în x = {x_interp} este {rezultat:.6f}")
