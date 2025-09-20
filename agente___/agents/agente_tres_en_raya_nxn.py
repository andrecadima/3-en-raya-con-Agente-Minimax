
from __future__ import annotations
from typing import Tuple, Literal, Callable
from math import inf
from agente___.algorithms.minimax_ab_eval import minimax_cutoff_ab
from agente___.algorithms.evaluation_nxn import evaluate_nxn
from agente___.environments.tres_en_raya_nxn import EntornoTresEnRayaNxN

Jugador = Literal["MAX", "MIN"]

def _accion_desde(parent: str, child: str) -> int:
    for i, (a, b) in enumerate(zip(parent, child)):
        if a != b:
            return i
    raise ValueError("Estados idénticos; no hay acción")

def make_eval_fn(n: int, k: int, me: str = "X", opp: str = "O") -> Callable[[str], float]:
    return lambda estado: evaluate_nxn(estado, n=n, win_k=k, me=me, opp=opp)

def mejor_jugada_nxn(env: EntornoTresEnRayaNxN, estado: str, jugador: Jugador = "MAX",
                      depth: int = 4, eval_fn: Callable[[str], float] | None = None
                      ) -> Tuple[int, str, float]:
    n, k = env.n, env.win_k
    if eval_fn is None:
        eval_fn = make_eval_fn(n, k)

    best_child = None
    best_val = -inf if jugador == "MAX" else inf

    hijos = list(env.sucesores(estado, jugador))
    for hijo in hijos:
        val = minimax_cutoff_ab(env, hijo, "MIN" if jugador == "MAX" else "MAX",
                                depth-1, -inf, inf, eval_fn)
        if jugador == "MAX":
            if val > best_val:
                best_val, best_child = val, hijo
        else:
            if val < best_val:
                best_val, best_child = val, hijo

    if best_child is None:
        return (-1, estado, env.utilidad(estado))
    accion = _accion_desde(estado, best_child)
    return (accion, best_child, best_val)
