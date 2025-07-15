from SimplexSolver import SimplexSolver
import numpy as np
import os

tamanho = 2000
tamanho2 = 1999

np.random.seed(42)
c = np.random.randint(10, 101, size=tamanho)
A = np.random.randint(1, 6, size=(tamanho, tamanho))
b = np.random.randint(200, 500, size=tamanho)
constraints = ['>='] * tamanho2 + ['<='] * (tamanho - tamanho2)

# Cria a pasta src se não existir
os.makedirs("src", exist_ok=True)

# Salva os dados no arquivo
with open("src/dados_entrada.txt", "w", encoding="utf-8") as f:
    f.write("Coeficientes da função objetivo (c):\n")
    f.write(np.array2string(c, separator=', ', threshold=np.inf) + "\n\n")

    f.write("Matriz de restrições (A):\n")
    f.write(np.array2string(A, separator=', ', threshold=np.inf) + "\n\n")

    f.write("Vetor do lado direito (b):\n")
    f.write(np.array2string(b, separator=', ', threshold=np.inf) + "\n\n")

    f.write("Tipos de restrições (constraints):\n")
    f.write(str(constraints) + "\n")


# Resolver o problema
try:
    solver = SimplexSolver(c, A, b, constraints, problem_type='min')
    solution, optimal_value = solver.solve()
    print("Solução ótima:", solution)
    print("Valor ótimo da função objetivo:", optimal_value)
except ValueError as e:
    print(e)
