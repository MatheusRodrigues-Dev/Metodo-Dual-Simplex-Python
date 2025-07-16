from typing import List, Dict
import pulp as pl


class KnapsackSolver:
    def __init__(self, values: List[float], weights: List[float], capacity: float):
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.n = len(values)
        self.model = pl.LpProblem("Knapsack", pl.LpMaximize)
        self.x = [pl.LpVariable(f"x{i}", cat="Binary") for i in range(self.n)]

        self._build_model()

    def _build_model(self):
        # Função objetivo
        self.model += pl.lpSum(self.values[i] * self.x[i]
                               for i in range(self.n)), "TotalValue"

        # Restrição de capacidade
        self.model += pl.lpSum(self.weights[i] * self.x[i]
                               for i in range(self.n)) <= self.capacity, "Capacity"

    def solve(self, solver: pl.LpSolver = None) -> Dict:
        solver = solver or pl.PULP_CBC_CMD(msg=False)
        self.model.solve(solver)

        selected_items = [i for i in range(
            self.n) if pl.value(self.x[i]) > 0.5]
        total_value = sum(self.values[i] for i in selected_items)
        total_weight = sum(self.weights[i] for i in selected_items)

        return {
            "status": pl.LpStatus[self.model.status],
            "selected_items": selected_items,
            "total_value": total_value,
            "total_weight": total_weight
        }

    def print_model_equations(self) -> None:
        print("Função objetivo:")
        obj = " + ".join([f"{self.values[i]}·x{i}" for i in range(self.n)])
        print(f"max z = {obj}")

        print("\nRestrição de capacidade:")
        cons = " + ".join([f"{self.weights[i]}·x{i}" for i in range(self.n)])
        print(f"      {cons} ≤ {self.capacity}")

        print("\nVariáveis de decisão:")
        for i in range(self.n):
            print(f"      x{i} ∈ {{0, 1}}")
