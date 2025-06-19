import numpy as np

def dual_simplex(c, A, b):
    """
    c: Coeficientes da função objetivo (1D array)
    A: Matriz de restrições (2D array)
    b: Lado direito das restrições (1D array)
    """

    # Ajusta sinais das restrições para <=
    for i in range(len(b)):
        if b[i] < 0:
            A[i, :] *= -1
            b[i] *= -1

    # Adiciona variáveis de folga
    slack = np.eye(A.shape[0])
    tableau = np.hstack((A, slack, b.reshape(-1, 1)))

    # Linha da função objetivo
    z_row = np.hstack((c, np.zeros(len(b) + 1)))  # +1 para coluna do lado direito

    tableau = np.vstack((z_row, tableau))

    # Dual Simplex Loop
    while any(tableau[1:, -1] < 0):  # enquanto tiver valor negativo no lado direito
        # Linha pivô: menor valor negativo no lado direito
        pivot_row = np.argmin(tableau[1:, -1]) + 1

        # Checagem se há coeficientes negativos na linha pivô
        candidates = np.where(tableau[pivot_row, :-1] < 0)[0]
        if len(candidates) == 0:
            raise Exception("Problema infactível!")

        # Calcula quocientes para encontrar pivô coluna
        quotients = tableau[0, candidates] / tableau[pivot_row, candidates]
        pivot_col = candidates[np.argmin(quotients)]

        # Gauss-Jordan Pivoteamento
        tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    # Extração de solução
    solution = np.zeros(len(c))
    for i in range(len(c)):
        col = tableau[1:, i]
        if list(col).count(1) == 1 and list(col).count(0) == len(col) - 1:
            one_row = np.where(col == 1)[0][0] + 1
            solution[i] = tableau[one_row, -1]

    optimal_value = tableau[0, -1]

    return solution, optimal_value
