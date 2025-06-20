from SimplexSolver import SimplexSolver

"""Exemplo primal mais dual
Situação:
Uma fábrica produz 2 produtos: A e B.

Lucro unitário:
    Produto A: R$3 por unidade.
    Produto B: R$5 por unidade.

Recursos disponíveis:
    Máquina 1: 4 horas disponíveis.
        Produto A consome 2h/unidade.
        Produto B consome 1h/unidade.
    Máquina 2: 6 horas disponíveis.
        Produto A consome 1h/unidade.
        Produto B consome 3h/unidade.

        
Definindo os coeficientes da função objetivo:
Exemplo: maximizar Lucro Z = 3x1 + 5x2
"""
c = [3, 5]

""" Definindo a matriz de restrições (A) e o vetor do lado direito (b):
Cada linha de A representa uma restrição.
Exemplo:
2x1 + 1x2 <= 4
1x1 + 3x2 <= 6
Assim, temos:"""

A = [[2, 1], [1, 3],]
b = [4, 6]

# Definindo o tipo de cada restrição:
# Use '<=' para menor ou igual, '>=' para maior ou igual, '=' para igualdade
constraints = ['<=', '<=']

print("=" * 100)
print("\nExemplo primal\n")

# Criando o resolvedor, informando se o problema é de minimização ('min') ou maximização ('max')
try:
    solver = SimplexSolver(c, A, b, constraints)
    solution, optimal_value = solver.solve()
    print("Solução ótima:", solution)
    print("Valor ótimo da função objetivo:", optimal_value)
except ValueError as e:
    print(e)  # Só imprime a mensagem personalizada


"""Resolução pelo Dual Simplex
Agora vamos inverter o problema (forma dual):

Restrições se tornam variáveis:
    y₁: custo hora Máquina 1
    y₂: custo hora Máquina 2
        
Definindo os coeficientes da função objetivo:
Exemplo: maximizar Lucro Z = 4y1 + 6y2
"""
c = [4, 6]

""" Definindo a matriz de restrições (A) e o vetor do lado direito (b):
Cada linha de A representa uma restrição.
Exemplo:
2y1 + 1y2 <= 3
1y1 + 3y2 <= 5
Assim, temos:"""

A = [[2, 1], [1, 3],]
b = [3, 5]

# Definindo o tipo de cada restrição:
# Use '<=' para menor ou igual, '>=' para maior ou igual, '=' para igualdade
constraints = ['>=', '>=']

print("=" * 100)
print("\nExemplo dual\n")

# Criando o resolvedor, informando se o problema é de minimização ('min') ou maximização ('max')
try:
    solver = SimplexSolver(c, A, b, constraints, problem_type='min')
    solution, optimal_value = solver.solve()
    print("Solução ótima:", solution)
    print("Valor ótimo da função objetivo:", optimal_value)
except ValueError as e:
    print(e)  # Só imprime a mensagem personalizada

