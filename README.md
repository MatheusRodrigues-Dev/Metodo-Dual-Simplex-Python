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

```python
c = np.array([6, 10, 5])
A = np.array([
    [1, 2, 3],
    [3, 0, 2]
])
b = np.array([24, 30])
constraints = ['<=', '<=']

solution, optimal_value = solve_linear_program(c, A, b, constraints, problem_type='max')
print("Solução ótima (Max):", solution)
print("Valor ótimo da função objetivo (Max):", optimal_value)

constraints_min = ['>=', '>=']
solution_min, optimal_value_min = solve_linear_program(c, A, b, constraints_min, problem_type='min')
print("Solução ótima (Min):", solution_min)
print("Valor ótimo da função objetivo (Min):", optimal_value_min)
```

## Observações

* Para problemas com mais de 2 variáveis não é possível gerar gráfico automático;
* Para visualização gráfica de problemas com 2 variáveis, é possível estender este código.

## Referências

* Pesquisa Operacional — Taha;
* Teoria e Implementação do Simplex Primal e Dual.

## Autor

Matheus Rodrigues

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
