from SimplexSolver import SimplexSolver

"""Resolução Simplex ultimo exemplo Aula 12

        
Definindo os coeficientes da função objetivo:
Exemplo: minimixar Z = 3000x1 + 2000x2 + 1930x3
"""
c = [2, 3, 4]

""" Definindo a matriz de restrições (A) e o vetor do lado direito (b):
Cada linha de A representa uma restrição.
Exemplo:
0.5x1 + 0.3x2 + 0.3x3≤ 3
0.1x1 + 0.2x2 + 0.3x3≤ 1
0.4x1 + 0.5x2 + 0.4x3≤ 3
Assim, temos:"""

A = [[4, 2, 1], [2, 1, 5], [2, 4, 4]]
b = [1000, 1040, 860]


# Definindo o tipo de cada restrição:
# Use '<=' para menor ou igual, '>=' para maior ou igual, '=' para igualdade
constraints = ['>=', '>=', '>=']

print("\nExemplo dual\n")

# Criando o resolvedor, informando se o problema é de minimização ('min') ou maximização ('max')
try:
    solver = SimplexSolver(c, A, b, constraints, problem_type='min')
    solution, optimal_value = solver.solve()
    print("Solução ótima:", solution)
    print("Valor ótimo da função objetivo:", optimal_value)
except ValueError as e:
    print(e)  # Só imprime a mensagem personalizada
