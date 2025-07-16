"""Solucionador exato para o Problema do Caixeiro‑Viajante (TSP) usando MTZ + visualização

Este script imprime de forma organizada:
  • Coordenadas numeradas das cidades
  • Matriz de distâncias euclidianas (2 casas)
  • Rota ótima no formato 1 → 2 → … → 1
  • Distância total
Gráficos com `matplotlib` são opcionais.
"""

from __future__ import annotations

from typing import List, Tuple, Sequence

import numpy as np
import pulp as pl
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import pandas as pd

# ------------ utilidades -----------------


def euclidean_matrix(coords: np.ndarray) -> np.ndarray:
    return np.round(cdist(coords, coords, metric="euclidean"), 2)


def distance_table(coords: np.ndarray):
    dist = euclidean_matrix(coords)
    n = len(coords)
    if pd is not None:
        labels = [f"{i+1}" for i in range(n)]
        df = pd.DataFrame(dist, index=labels, columns=labels)
        print("\nMatriz de distâncias euclidianas (usando pandas):")
        print(df)
        return df
    # Print manual, caso pandas não esteja disponível
    print("\nMatriz de distâncias euclidianas:")
    header = "     " + " ".join(f"{j+1:>7}" for j in range(n))
    print(header)
    print("    " + "-" * (8 * n))
    for i in range(n):
        row = f"{i+1:>3} |" + "".join(f"{dist[i][j]:8.2f}" for j in range(n))
        print(row)
    return dist

# ------------ visualização ---------------


def plot_points(coords, title="Cidades"):
    if plt is None:
        return
    plt.figure()
    plt.scatter(coords[:, 0], coords[:, 1], c="black")
    for i, (x, y) in enumerate(coords):
        plt.text(x+1, y+1, str(i+1))
    plt.title(title)
    plt.axis("equal")
    plt.show()


def plot_route(coords, route, title="Rota"):
    if plt is None:
        return
    plt.figure()
    plt.scatter(coords[:, 0], coords[:, 1], c="black")
    for i, (x, y) in enumerate(coords):
        plt.text(x+1, y+1, str(i+1))
    for k in range(len(route)-1):
        i, j = route[k], route[k+1]
        plt.plot([coords[i, 0], coords[j, 0]], [coords[i, 1], coords[j, 1]])
    plt.title(title)
    plt.axis("equal")
    plt.show()

# ------------ solver MTZ -----------------


def solve_tsp_mtz(dist: np.ndarray, solver: pl.LpSolver | None = None):
    n = dist.shape[0]
    m = pl.LpProblem("TSP", pl.LpMinimize)
    x = pl.LpVariable.dicts("x", (range(n), range(n)), 0, 1, pl.LpBinary)
    u = pl.LpVariable.dicts("u", range(n), 0, n-1, pl.LpContinuous)
    m += pl.lpSum(dist[i][j]*x[i][j]
                  for i in range(n) for j in range(n) if i != j)
    for i in range(n):
        m += pl.lpSum(x[i][j] for j in range(n) if j != i) == 1
        m += pl.lpSum(x[j][i] for j in range(n) if j != i) == 1
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                m += u[i]-u[j]+(n-1)*x[i][j] <= n-2
    m.solve(solver or pl.PULP_CBC_CMD(msg=False))
    tour = [0]
    while True:
        cur = tour[-1]
        nxt = next(j for j in range(n) if j !=
                   cur and pl.value(x[cur][j]) == 1)
        tour.append(nxt)
        if nxt == 0:
            break
    total = pl.value(m.objective)

    # Prints melhorados
    print("\n=== Problema do Caixeiro Viajante (TSP) ===")
    print(f"Número de cidades: {n}")
    print("\nMatriz de distâncias:")
    for i in range(n):
        print(" ".join(f"{dist[i][j]:6.2f}" for j in range(n)))
    print("\nRota ótima encontrada:")
    print(" → ".join(str(c+1) for c in tour))
    print(f"\nDistância total da rota: {total:.2f}\n")
    return tour, total
