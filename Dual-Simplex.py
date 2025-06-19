import numpy as np


def primal_simplex(c, A, b):
    """Primal Simplex para problemas já factíveis"""
    slack = np.eye(A.shape[0])
    tableau = np.hstack((A, slack, b.reshape(-1, 1)))
    z_row = np.hstack((-c, np.zeros(len(b) + 1)))
    tableau = np.vstack((z_row, tableau))

    while any(tableau[0, :-1] < 0):
        pivot_col = np.argmin(tableau[0, :-1])
        if all(tableau[1:, pivot_col] <= 0):
            raise Exception("Problema ilimitado!")
        ratios = []
        for i in range(1, tableau.shape[0]):
            if tableau[i, pivot_col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, pivot_col])
            else:
                ratios.append(np.inf)
        pivot_row = np.argmin(ratios) + 1

        tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    solution = np.zeros(len(c))
    for i in range(len(c)):
        col = tableau[1:, i]
        if list(col).count(1) == 1 and list(col).count(0) == len(col) - 1:
            one_row = np.where(col == 1)[0][0] + 1
            solution[i] = tableau[one_row, -1]

    optimal_value = tableau[0, -1]
    return solution, -optimal_value


def dual_simplex(c, A, b):
    """Dual Simplex usado quando a solução inicial é ótima mas infactível"""
    slack = np.eye(A.shape[0])
    tableau = np.hstack((A, slack, b.reshape(-1, 1)))
    z_row = np.hstack((c, np.zeros(len(b) + 1)))
    tableau = np.vstack((z_row, tableau))

    while any(tableau[1:, -1] < 0):
        pivot_row = np.argmin(tableau[1:, -1]) + 1
        candidates = np.where(tableau[pivot_row, :-1] < 0)[0]
        if len(candidates) == 0:
            raise Exception("Problema infactível!")
        quotients = tableau[0, candidates] / tableau[pivot_row, candidates]
        pivot_col = candidates[np.argmin(quotients)]
        tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

    solution = np.zeros(len(c))
    for i in range(len(c)):
        col = tableau[1:, i]
        if list(col).count(1) == 1 and list(col).count(0) == len(col) - 1:
            one_row = np.where(col == 1)[0][0] + 1
            solution[i] = tableau[one_row, -1]

    optimal_value = tableau[0, -1]
    return solution, optimal_value


def solve_linear_program(c, A, b, constraints, problem_type='max'):
    """
    constraints: lista de strings ['<=', '>=', '='] indicando o tipo de cada restrição
    """
    A_new = A.copy()
    b_new = b.copy()

    for i, constr in enumerate(constraints):
        if constr == '>=':
            A_new[i, :] *= -1
            b_new[i] *= -1

    if problem_type == 'min':
        c = -c

    # Verifica qual método aplicar
    if all(b_new >= 0):
        print("Usando Primal Simplex")
        solution, optimal_value = primal_simplex(c, A_new, b_new)
    else:
        print("Usando Dual Simplex")
        solution, optimal_value = dual_simplex(c, A_new, b_new)

    if problem_type == 'min':
        optimal_value = -optimal_value

    return solution, optimal_value


# Exemplo de uso
c = np.array([6, 10, 5])

A = np.array([
    [1, 2, 3],
    [3, 0, 2]
])
b = np.array([24, 30])
constraints = ['<=', '<=']

solution, optimal_value = solve_linear_program(
    c, A, b, constraints, problem_type='max')
print("Solução ótima (Max):", solution)
print("Valor ótimo da função objetivo (Max):", optimal_value)

constraints_min = ['>=', '>=']
solution_min, optimal_value_min = solve_linear_program(
    c, A, b, constraints_min, problem_type='min')
print("Solução ótima (Min):", solution_min)
print("Valor ótimo da função objetivo (Min):", optimal_value_min)
