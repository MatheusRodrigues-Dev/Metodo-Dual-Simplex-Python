from SimplexSolver import SimplexSolver

"""Resolução pelo Dual Simplex

        
Definindo os coeficientes da função objetivo:
Exemplo: minimixar Z = 2000x1 + 6000x2
"""
c = [2000, 6000]

""" Definindo a matriz de restrições (A) e o vetor do lado direito (b):
Cada linha de A representa uma restrição.
Exemplo:
x1 +3x2 ≤ 15
2x1 + 4x2 ≤ 20
16x1 + 8x2 ≤ 30
Assim, temos:"""

A = [[1, 3], [2, 4], [16, 8]]
b = [15, 20, 30]


# Definindo o tipo de cada restrição:
# Use '<=' para menor ou igual, '>=' para maior ou igual, '=' para igualdade
constraints = ['<=', '<=', '<=']

print("\nExemplo dual\n")

# Criando o resolvedor, informando se o problema é de minimização ('min') ou maximização ('max')
try:
    solver = SimplexSolver(c, A, b, constraints, problem_type='max')
    solution, optimal_value = solver.solve()
    print("Solução ótima:", solution)
    print("Valor ótimo da função objetivo:", optimal_value)
except ValueError as e:
    print(e)  # Só imprime a mensagem personalizada

