# Método Simplex (Primal e Dual) — Implementação em Python

## 📘 Descrição

Este projeto implementa o **Método Simplex Primal e Dual** para resolução de problemas de **Programação Linear (PL)** e **Programação Inteira (PI)**. Além disso, foram incluídas implementações para resolver problemas clássicos de Pesquisa Operacional:

* ✅ Problema da **Mochila 0-1**
* ✅ Problema do **Caixeiro-Viajante**
* ✅ Problema de **Orçamento de Capital**
* ✅ Problema de **Localização de Facilidades** (com capacidade e custo fixo)

---

## ⚙️ Funcionalidades

* ✔️ Resolve problemas de **maximização** e **minimização**;
* ✔️ Suporta restrições `<=`, `>=` e `=`;
* ✔️ Adiciona automaticamente variáveis de folga, excesso e artificiais;
* ✔️ Executa pivoteamento Gauss-Jordan com seleção automática do método: **Primal** ou **Dual**;
* ✔️ Suporte a modelagens com variáveis binárias e inteiras (via `Pulp`);
* ✔️ Visualização de resultados e rotas com gráficos (usando `Matplotlib`);
* ✔️ Cálculo e exibição da **função objetivo simbólica** para interpretação.

---

## 📂 Estrutura do Projeto

```
├── classes/
│   └── ClassCaixerio.py   # Contém a clases do caixeiro viajante com funções auxiliares
│   └── ClassMochila.py    # Contém a clases da mochila com funções auxiliares
│   └── SimplexSolver.py   # Contém a clases para resolver o simplex ou o dual simplex e com funções auxiliares
├── dual-simplex.ipynb        # Problema da Mochila com visualização
├── mochila.ipynb             # Problema da Mochila com visualização
├── caixeiro.ipynb            # Caixeiro-Viajante com solver MTZ
├── investimento.ipynb        # Modelo binário de orçamento de capital
└── localizacao.ipynb         # Problema de localização de facilidades
├── src/
│   └── *.xlsx / *.csv         # Dados opcionais para testes ou importação
└── README.md
```

---

## 🧮 Entradas esperadas pelo Simplex

```python
c = [...]               # Coeficientes da função objetivo
A = [[...], [...]]      # Matriz de coeficientes das restrições
b = [...]               # Termos do lado direito das restrições
constraints = ['<=', '>=', '=']  # Lista de sinais
problem_type = 'max' or 'min'    # Tipo do problema
```

---

## 🧠 Exemplos Resolvidos

### 🎒 Problema da Mochila

Seleciona os itens mais valiosos dentro de um limite de peso usando programação inteira binária. Inclui:

* Lista de objetos, pesos e utilidades
* Visualização da solução
* Classe Python reutilizável para diferentes instâncias

### 📍 Problema do Caixeiro-Viajante (TSP)

Busca o caminho mínimo que passa por todas as cidades exatamente uma vez e retorna à origem. Inclui:

* Formulação com restrições MTZ
* Gráfico com as rotas e subrotas
* Solução exata via Pulp

### 💰 Problema de Investimento (Orçamento de Capital)

Modelo binário para seleção de projetos sob restrição orçamentária, maximizando o VPL:

* Entrada via listas
* Saída com projetos escolhidos e função objetivo simbólica

### 🏭 Localização de Facilidades

Seleciona fábricas que devem ser abertas, minimizando custo fixo + transporte, respeitando capacidade e demanda.

---

## 💻 Requisitos

* Python 3.x
* Bibliotecas:

```bash
pip install numpy pulp matplotlib pandas scipy
```

---

## 📊 Funcionamento do Método Simplex

1. **Pré-processamento:** adapta o problema para o formato padrão (max, RHS positivo)
2. **Seleção do Método:** aplica Primal ou Dual com base na viabilidade inicial
3. **Resolução iterativa:** realiza pivoteamento até encontrar solução ótima
4. **Saída:** apresenta valores ótimos e identifica o método utilizado

---

## 📎 Observações

* Problemas com **duas variáveis** podem ser representados graficamente.
* Para problemas inteiros e binários, o projeto utiliza o solver **Pulp + CBC**.
* Para o TSP e Localização de Facilidades, foram utilizados algoritmos exatos e heurísticas.

---

## 📚 Referências

* Taha, H. A. – Pesquisa Operacional
* Hillier & Lieberman – Introduction to Operations Research
* Chopra & Meindl – Supply Chain Management
* Documentação oficial do [`Pulp`](https://coin-or.github.io/pulp/)

---

## 👨‍💻 Autor

**Matheus Rodrigues**
Projeto acadêmico para fins didáticos — Engenharia de Produção / Pesquisa Operacional