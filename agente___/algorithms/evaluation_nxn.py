
from __future__ import annotations
from math import inf
from typing import Callable

def evaluate_nxn(estado: str, n: int, win_k: int, me: str = "X", opp: str = "O") -> float:
    """
    Heurística para NxN conecta-K:
    - ±inf si terminal (ganar/perder).
    - Suma/resta por cada ventana de tamaño K que esté "abierta" (sin fichas del rival),
      ponderando más las que tienen K-1, luego K-2, etc.
    - Pequeño bonus por centro.
    """
    # Terminales
    if _gana(estado, n, win_k, me):  return inf
    if _gana(estado, n, win_k, opp): return -inf
    if "." not in estado:            return 0.0

    # Ponderaciones: más fuerte para (K-1) que para 1
    # w[t] = 10^(t-1), t = cantidad de mis fichas en la ventana (1..K-1)
    weights = [0.0] + [10.0**(t-1) for t in range(1, win_k)]  # index by t

    score = 0.0
    grid = [estado[i*n:(i+1)*n] for i in range(n)]

    def score_window(cells):
        mc = sum(1 for x in cells if x == me)
        oc = sum(1 for x in cells if x == opp)
        if oc == 0 and mc > 0:
            return weights[mc]
        if mc == 0 and oc > 0:
            return -weights[oc]
        return 0.0

    # Horizontal
    for r in range(n):
        for c in range(n - win_k + 1):
            cells = [grid[r][c+j] for j in range(win_k)]
            score += score_window(cells)
    # Vertical
    for c in range(n):
        for r in range(n - win_k + 1):
            cells = [grid[r+j][c] for j in range(win_k)]
            score += score_window(cells)
    # Diagonal principal
    for r in range(n - win_k + 1):
        for c in range(n - win_k + 1):
            cells = [grid[r+j][c+j] for j in range(win_k)]
            score += score_window(cells)
    # Diagonal secundaria
    for r in range(n - win_k + 1):
        for c in range(win_k - 1, n):
            cells = [grid[r+j][c-j] for j in range(win_k)]
            score += score_window(cells)

    # Centro (ligero)
    center_idx = (n*n)//2
    if estado[center_idx] == me:  score += 0.5
    if estado[center_idx] == opp: score -= 0.5

    return score

def _gana(estado: str, n: int, k: int, p: str) -> bool:
    grid = [estado[i*n:(i+1)*n] for i in range(n)]
    # Horizontal/vertical
    for r in range(n):
        for c in range(n-k+1):
            if all(grid[r][c+j] == p for j in range(k)): return True
    for c in range(n):
        for r in range(n-k+1):
            if all(grid[r+j][c] == p for j in range(k)): return True
    # Diagonales
    for r in range(n-k+1):
        for c in range(n-k+1):
            if all(grid[r+j][c+j] == p for j in range(k)): return True
    for r in range(n-k+1):
        for c in range(k-1, n):
            if all(grid[r+j][c-j] == p for j in range(k)): return True
    return False
