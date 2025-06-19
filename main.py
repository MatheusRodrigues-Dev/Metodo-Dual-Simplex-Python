# Exemplo de uso
from SimplexSolver import SimplexSolver

c = [6, 4]
A = [
    [9, 3],
    [4, 8]
]
b = [1500, 1600]
constraints = ['>=', '>=']

solver = SimplexSolver(c, A, b, constraints, problem_type='min')
solution, optimal_value = solver.solve()
print("Solução ótima:", solution)
print("Valor ótimo da função objetivo:", optimal_value)