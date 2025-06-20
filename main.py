from SimplexSolver import SimplexSolver

""" Exemplo baseado no artigo:
 https://medium.com/@minkyunglee_5476/linear-programming-the-dual-simplex-method-d3ab832afc50

Definindo os coeficientes da função objetivo:
Exemplo: minimizar Z = 3x1 + 2x2
"""
c = [3, 2]
""" Definindo a matriz de restrições (A) e o vetor do lado direito (b):
Cada linha de A representa uma restrição.
Exemplo:
3x1 + 2x2 <= 60
1x1 + 4x2 <= 20
3x1 + 4x2 <= 50
1x1 + 2x2 >= 10
Assim, temos:"""
A = [
    [3, 2],
    [1, 4],
    [3, 4],
    [1, 2]
]
b = [60, 20, 50, 10]

# Definindo o tipo de cada restrição:
# Use '<=' para menor ou igual, '>=' para maior ou igual, '=' para igualdade
constraints = ['<=', '<=', '<=', '>=']

# Criando o resolvedor, informando se o problema é de minimização ('min') ou maximização ('max')
try:
    solver = SimplexSolver(c, A, b, constraints, problem_type='min')
    solution, optimal_value = solver.solve()
    print("Solução ótima:", solution)
    print("Valor ótimo da função objetivo:", optimal_value)
except ValueError as e:
    print(e)  # Só imprime a mensagem personalizada
    