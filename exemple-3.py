from SimplexSolver import SimplexSolver

"""Resolução pelo Dual Simplex

        
Definindo os coeficientes da função objetivo:
Exemplo: minimixar Z = 5x1 + 2x2
"""
c = [5, 2]

""" Definindo a matriz de restrições (A) e o vetor do lado direito (b):
Cada linha de A representa uma restrição.
Exemplo:
6x1 +2 x2 ≥ 66
2x1 + 4x2 ≥ 36
2x1 + 5x2 ≤ 40
Assim, temos:"""

A = [[6, 2], [2, 4], [2, 5]]
b = [66, 36, 40]

# Definindo o tipo de cada restrição:
# Use '<=' para menor ou igual, '>=' para maior ou igual, '=' para igualdade
constraints = ['>=', '>=', '<=']

print("\nExemplo dual\n")

# Criando o resolvedor, informando se o problema é de minimização ('min') ou maximização ('max')
try:
    solver = SimplexSolver(c, A, b, constraints, problem_type='min')
    solution, optimal_value = solver.solve()
    print("Solução ótima:", solution)
    print("Valor ótimo da função objetivo:", optimal_value)
except ValueError as e:
    print(e)  # Só imprime a mensagem personalizada

