import numpy as np


class SimplexSolver:
    """
    Classe para resolver problemas de Programação Linear usando os métodos Simplex Primal e Dual.
    """

    def __init__(self, c, A, b, constraints, problem_type='max'):
        """
        Inicializa o resolvedor com os parâmetros do problema.

        :param c: Vetor de custos (função objetivo)
        :param A: Matriz de restrições
        :param b: Vetor do lado direito das restrições
        :param constraints: Lista de strings com os tipos de restrição ('>=', '<=', '=')
        :param problem_type: 'max' para maximização, 'min' para minimização
        """
        if len(constraints) != len(b):
            raise ValueError(
                f"O número de restrições em 'constraints' ({len(constraints)}) deve ser igual ao tamanho de 'b' ({len(b)})."
            )
        self.c = np.array(c, dtype=float)
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.constraints = constraints
        self.problem_type = problem_type

    def print_tableau(self, tableau, basic_vars, var_names, iteration):
        """Imprime o tableau atual com variáveis básicas e número da iteração, formatado"""
        print(f"\nTableau - Iteração {iteration}:")
        # # Cabeçalho alinhado
        # header = ["    "] + [f"{v:>8}" for v in var_names] + [f"{'LD':>8}"]
        # print("".join(header))
        # print("-" * (9 * (len(var_names) + 2)))  # Ajuste do separador

        # for i, row in enumerate(tableau):
        #     if i == 0:
        #         var = "  Z "
        #     else:
        #         var = f"{basic_vars[i-1]:>4}"
        #     # Valores alinhados com 2 casas decimais e espaçamento
        #     row_str = "".join([f"{v:9.2f}" for v in row])
        #     print(f"{var}{row_str}")
        #     print("-" * (9 * (len(var_names) + 2)))

    def primal_simplex(self, c, A, b):
        """
        Resolve o problema pelo método Simplex Primal.
        """
        slack = np.eye(A.shape[0])
        tableau = np.hstack((A, slack, b.reshape(-1, 1)))
        z_row = np.hstack((-c, np.zeros(len(b) + 1)))
        tableau = np.vstack((z_row, tableau))

        var_names = [
            f"x{i+1}" for i in range(len(c))] + [f"s{i+1}" for i in range(len(b))]
        basic_vars = [f"s{i+1}" for i in range(len(b))]

        iteration = 0
        self.print_tableau(tableau, basic_vars, var_names, iteration)

        while any(tableau[0, :-1] < 0):
            iteration += 1
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

            basic_vars[pivot_row - 1] = var_names[pivot_col]

            tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
            for i in range(tableau.shape[0]):
                if i != pivot_row:
                    tableau[i, :] -= tableau[i, pivot_col] * \
                        tableau[pivot_row, :]

            self.print_tableau(tableau, basic_vars, var_names, iteration)

        solution = np.zeros(len(c))
        for i in range(len(c)):
            col = tableau[1:, i]
            if list(col).count(1) == 1 and list(col).count(0) == len(col) - 1:
                one_row = np.where(col == 1)[0][0] + 1
                solution[i] = tableau[one_row, -1]

        optimal_value = tableau[0, -1]
        return solution, optimal_value

    def dual_simplex(self, c, A, b):
        """
        Resolve o problema pelo método Simplex Dual.
        """
        slack = np.eye(A.shape[0])
        tableau = np.hstack((A, slack, b.reshape(-1, 1)))
        z_row = np.hstack((c, np.zeros(len(b) + 1)))
        tableau = np.vstack((z_row, tableau))

        var_names = [
            f"x{i+1}" for i in range(len(c))] + [f"s{i+1}" for i in range(len(b))]
        basic_vars = [f"s{i+1}" for i in range(len(b))]

        iteration = 0
        self.print_tableau(tableau, basic_vars, var_names, iteration)

        while any(tableau[1:, -1] < 0):
            iteration += 1
            pivot_row = np.argmin(tableau[1:, -1]) + 1
            candidates = np.where(tableau[pivot_row, :-1] < 0)[0]
            if len(candidates) == 0:
                raise Exception("Problema infactível!")
            quotients = tableau[0, candidates] / tableau[pivot_row, candidates]
            pivot_col = candidates[np.argmin(quotients)]

            basic_vars[pivot_row - 1] = var_names[pivot_col]

            tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
            for i in range(tableau.shape[0]):
                if i != pivot_row:
                    tableau[i, :] -= tableau[i, pivot_col] * \
                        tableau[pivot_row, :]

            self.print_tableau(tableau, basic_vars, var_names, iteration)

        solution = np.zeros(len(c))
        for i in range(len(c)):
            col = tableau[1:, i]
            if list(col).count(1) == 1 and list(col).count(0) == len(col) - 1:
                one_row = np.where(col == 1)[0][0] + 1
                solution[i] = tableau[one_row, -1]

        optimal_value = tableau[0, -1]
        return solution, optimal_value

    def solve(self):
        """
        Resolve o problema de PL usando o método apropriado (Primal ou Dual).
        """
        A_new = self.A.copy()
        b_new = self.b.copy()
        c = self.c.copy()

        # Ajusta restrições do tipo '>=' para '<='
        for i, constr in enumerate(self.constraints):
            if constr == '>=':
                A_new[i, :] *= -1
                b_new[i] *= -1

        if self.problem_type == 'min':
            c = -c

        if all(b_new >= 0):
            print("Usando Primal Simplex")
            solution, optimal_value = self.primal_simplex(c, A_new, b_new)
        else:
            print("Usando Dual Simplex")
            solution, optimal_value = self.dual_simplex(c, A_new, b_new)

        # if self.problem_type == 'min':
        #     optimal_value = -optimal_value

        return solution, optimal_value
