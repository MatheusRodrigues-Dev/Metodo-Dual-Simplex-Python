from SimplexSolver import SimplexSolver

"""Resolução pelo Dual Simplex

        
Definindo os coeficientes da função objetivo:
Exemplo: minimixar Z = 3x1 + 2x2 + x3
"""
c = [3, 2, 1]

""" Definindo a matriz de restrições (A) e o vetor do lado direito (b):
Cada linha de A representa uma restrição.
Exemplo:
3x1 + x2 + x3 >= 3
-3x1 + 3x2 + x3 >= 6
x1 + x2 + x3 <= 3
x1, x2, x3 >=0
Assim, temos:"""

A = [[3, 1, 1], [-3, 3, 1], [1, 1, 1]]
b = [3, 6, 3]

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

