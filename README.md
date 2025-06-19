# Método Simplex (Primal e Dual) — Implementação em Python

## Descrição

Este projeto implementa tanto o **método Primal Simplex** quanto o **método Dual Simplex** para resolução de problemas de Programação Linear (PL). O algoritmo decide automaticamente qual método aplicar com base na factibilidade inicial das restrições.

## Funcionalidades

✔️ Resolve problemas de **maximização** e **minimização**;
✔️ Suporta restrições do tipo `<=`, `>=` e `=`;
✔️ Adiciona variáveis de folga, excesso e artificiais automaticamente;
✔️ Executa pivoteamento Gauss-Jordan;
✔️ Retorna solução ótima e valor da função objetivo;
✔️ Informa no console qual método foi aplicado: **Primal ou Dual Simplex**.

## O que o código espera como entrada?

* **`c`** — Vetor de coeficientes da função objetivo;
* **`A`** — Matriz dos coeficientes das restrições;
* **`b`** — Vetor dos termos independentes (lado direito das restrições);
* **`constraints`** — Lista indicando o sinal de cada restrição: `['<=', '>=', '=']`;
* **`problem_type`** — Tipo do problema: `'max'` ou `'min'`.

## Pré-requisitos

* Python 3.x
* Biblioteca NumPy:

```bash
pip install numpy
```

## Funcionamento do Algoritmo

1. **Preparação do Problema:**

   * As restrições são ajustadas automaticamente para o formato adequado;
   * As desigualdades `>=` são multiplicadas por -1;
   * O problema de minimização é convertido para maximização, se necessário.

2. **Seleção do Método:**

   * Se o lado direito (`b`) já for factível (todos valores >= 0): usa **Primal Simplex**;
   * Caso contrário: usa **Dual Simplex**;
   * O método escolhido é exibido no console.

3. **Resolução:**

   * Realiza pivoteamento de Gauss-Jordan iterativamente até encontrar a solução ótima.

4. **Solução Final:**

   * Retorna os valores das variáveis e o valor ótimo da função objetivo.

## Exemplo de Uso

Crie uma instância da classe passando:
   - `c`: lista ou array com os coeficientes da função objetivo.
   - `A`: matriz das restrições.
   - `b`: lista ou array com o lado direito das restrições.
   - `constraints`: lista com os tipos de restrição (`'>='`, `'<='`, `'='`).
   - `problem_type`: `'max'` para maximização ou `'min'` para minimização.

   ```python
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
   ```

## Observações

* Para problemas com mais de 2 variáveis não é possível gerar gráfico automático;
* Para visualização gráfica de problemas com 2 variáveis, é possível estender este código.

## Referências

* Pesquisa Operacional — Taha;
* Teoria e Implementação do Simplex Primal e Dual.

## Autor

Matheus Rodrigues
