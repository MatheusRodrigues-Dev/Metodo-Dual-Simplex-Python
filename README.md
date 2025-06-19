# Método Dual Simplex — Implementação em Python

## Descrição

Este projeto implementa o **método Dual Simplex** para resolução de problemas de Programação Linear (PL). O método é utilizado quando a solução inicial é **ótima mas infactível**, sendo uma alternativa ao método Primal Simplex tradicional.

## Funcionalidades

✔️ Resolve problemas de maximização ou minimização;
✔️ Aceita funções objetivo e restrições arbitrárias;
✔️ Manipula automaticamente restrições `<=`, `>=` e `=`;
✔️ Adiciona variáveis de folga, excesso e artificiais (se necessário);
✔️ Executa pivoteamento Gauss-Jordan;
✔️ Retorna solução ótima e valor da função objetivo.

## O que o código espera como entrada?

* **`c`** — Vetor de coeficientes da função objetivo (excluindo variáveis de folga/artificiais);
* **`A`** — Matriz dos coeficientes das restrições;
* **`b`** — Vetor dos termos independentes (lado direito das restrições).

## Pré-requisitos

* Python 3.x
* Biblioteca NumPy:

```bash
pip install numpy
```

## Funcionamento do Algoritmo

1. **Preparação do Problema:**

   * As restrições são ajustadas para o formato padrão (`<=`);
   * São adicionadas variáveis de folga conforme necessário.

2. **Construção da Tabela Simplex:**

   * É montada a tabela (tableau) com variáveis básicas e função objetivo.

3. **Iterações do Dual Simplex:**

   * Identifica a linha pivô com o menor valor negativo no lado direito;
   * Seleciona a coluna pivô com o menor quociente `c_j/a_rj`;
   * Executa o pivoteamento (eliminação de Gauss-Jordan);
   * Repete até que não haja mais valores negativos no lado direito.

4. **Solução Final:**

   * O algoritmo retorna a solução ótima encontrada e o valor da função objetivo.

## Exemplo de Uso

```python
import numpy as np
from dual_simplex import dual_simplex

# Coeficientes da função objetivo
c = np.array([-3, -5])  # Exemplo: Max Z = 3x + 5y

# Matriz de restrições
A = np.array([
    [1, 2],
    [4, 0],
    [0, 4]
])

# Lado direito das restrições
b = np.array([8, 16, 12])

# Chamada do método
solution, optimal_value = dual_simplex(c, A, b)

print("Solução ótima:", solution)
print("Valor ótimo da função objetivo:", optimal_value)
```

## Referências

* Pseudo-código baseado em literatura de Pesquisa Operacional;
* Métodos de Programação Linear: Primal e Dual Simplex;
* Introdução à Pesquisa Operacional – Taha.

## Autor

Matheus Rodrigues

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
