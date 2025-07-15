from SimplexSolver import SimplexSolver

""" Exemplo baseado no artigo:
 https://medium.com/@minkyunglee_5476/linear-programming-the-dual-simplex-method-d3ab832afc50

Definindo os coeficientes da função objetivo:
Exemplo: minimizar Z = 3x1 + 2x2
"""
c = [22, 18, 26, 30, 15, 20, 17, 19, 25, 24]
""" Definindo a matriz de restrições (A) e o vetor do lado direito (b):
Cada linha de A representa uma restrição.
Exemplo:
3x1 + 2x2 <= 60
1x1 + 4x2 <= 20
3x1 + 4x2 <= 50
1x1 + 2x2 >= 10
Assim, temos:"""
A = [
    [2, 1, 3, 0, 5, 4, 0, 0, 2, 1],
    [1, 3, 0, 2, 1, 0, 5, 4, 0, 0],
    [0, 2, 1, 3, 4, 0, 0, 1, 2, 3],
    [3, 0, 2, 1, 1, 3, 2, 0, 0, 1],
    [4, 2, 0, 0, 3, 1, 1, 2, 2, 0],
    [2, 3, 1, 0, 0, 1, 0, 3, 1, 2],
    [1, 0, 0, 4, 2, 2, 1, 1, 3, 2],
    [0, 1, 2, 2, 3, 0, 4, 0, 2, 1],
    [3, 2, 1, 1, 1, 2, 0, 3, 1, 0],
    [1, 0, 3, 2, 0, 4, 2, 2, 0, 3]
]

# Definindo o tipo de cada restrição:
# Use '<=' para menor ou igual, '>=' para maior ou igual, '=' para igualdade
constraints = ['>=', '>=', '>=', '>=', '>=', '>=', '>=', '>=', '>=', '>=']

b = [120, 100, 90, 110, 130, 95, 105, 100, 125, 115]

# Criando o resolvedor, informando se o problema é de minimização ('min') ou maximização ('max')
try:
    solver = SimplexSolver(c, A, b, constraints, problem_type='min')
    solution, optimal_value = solver.solve()
    print("Solução ótima:", solution)
    print("Valor ótimo da função objetivo:", optimal_value)
except ValueError as e:
    print(e)  # Só imprime a mensagem personalizada
    