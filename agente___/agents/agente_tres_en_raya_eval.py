
from __future__ import annotations
from typing import Tuple, Literal, Callable
from math import inf
from agente___.algorithms.minimax_ab_eval import minimax_cutoff_ab
from agente___.algorithms.evaluation import evaluate_tres_en_raya
from agente___.environments.tres_en_raya import EntornoTresEnRaya

Jugador = Literal["MAX", "MIN"]

def _accion_desde(parent: str, child: str) -> int:
    for i, (a, b) in enumerate(zip(parent, child)):
        if a != b:
            return i
    raise ValueError("Estados idénticos; no hay acción")

def mejor_jugada_eval(env: EntornoTresEnRaya, estado: str, jugador: Jugador = "MAX",
                      depth: int = 4, eval_fn: Callable[[str], float] = evaluate_tres_en_raya
                      ) -> Tuple[int, str, float]:
    """
    Devuelve (accion_index, estado_hijo, valor) usando minimax con alfa-beta + cutoff.
    depth=4 es suficiente para 3x3 y muy rápido; puedes subirlo o bajarlo.
    """
    best_child = None
    best_val = -inf if jugador == "MAX" else inf

    hijos = list(env.sucesores(estado, jugador) if hasattr(env, "sucesores") else env.sucesores(estado))
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
        # No hay movimientos (debería ser terminal)
        return (-1, estado, env.utilidad(estado))
    accion = _accion_desde(estado, best_child)
    return (accion, best_child, best_val)
