
# agente___/algorithms/minimax_ab_eval.py
from __future__ import annotations
from typing import Protocol, Any, Iterable, Optional, Callable, Literal
from math import inf

Jugador = Literal["MAX", "MIN"]

class EntornoMinimax(Protocol):
    def es_terminal(self, estado: Any) -> bool: ...
    def utilidad(self, estado: Any) -> float: ...
    # sucesores puede ser sucesores(estado) o sucesores(estado, jugador)

def _sucesores(env: Any, estado: Any, jugador: Jugador) -> Iterable[Any]:
    try:
        return env.sucesores(estado, jugador)
    except TypeError:
        return env.sucesores(estado)

EvalFn = Callable[[Any], float]

def minimax_cutoff_ab(env: EntornoMinimax, estado: Any, jugador: Jugador,
                      depth: int, alpha: float, beta: float, eval_fn: EvalFn) -> float:
    """
    Minimax con poda alfa-beta y profundidad máxima (cutoff).
    Usa eval_fn en el cutoff.
    """
    if env.es_terminal(estado) or depth == 0:
        if env.es_terminal(estado):
            return env.utilidad(estado)
        return eval_fn(estado)

    if jugador == "MAX":
        v = -inf
        for hijo in _sucesores(env, estado, "MAX"):
            v = max(v, minimax_cutoff_ab(env, hijo, "MIN", depth-1, alpha, beta, eval_fn))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = inf
        for hijo in _sucesores(env, estado, "MIN"):
            v = min(v, minimax_cutoff_ab(env, hijo, "MAX", depth-1, alpha, beta, eval_fn))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v
