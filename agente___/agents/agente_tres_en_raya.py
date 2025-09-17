from __future__ import annotations
from typing import Dict, Optional, Tuple, Literal
from agente___.algorithms.minimax_simple import MiniMax
from agente___.environments.tres_en_raya import EntornoTresEnRaya

Jugador = Literal["MAX","MIN"]

def _accion_desde(parent: str, child: str) -> int:
    # Devuelve el índice (0..8) donde cambió el estado
    for i, (a, b) in enumerate(zip(parent, child)):
        if a != b:
            return i
    raise ValueError("Estados idénticos; no hay acción")

def mejor_jugada(env: EntornoTresEnRaya, estado: str, jugador: Jugador = "MAX"
                 ) -> Tuple[int, str, float]:
    """
    Devuelve (accion_idx, estado_hijo, valor) para el 'jugador' dado.
    Usa el MiniMax ya implementado y etiquetas precalculadas para elegir óptimo.
    """
    etiquetas: Dict[str, float] = {}
    _ = MiniMax(env, estado, jugador, etiquetas)  # etiqueta todo

    if jugador == "MAX":
        best_val, best_child = float("-inf"), None
        for child in env.sucesores(estado, "MAX"):
            v = etiquetas.get(child)
            if v is None:
                v = MiniMax(env, child, "MIN")
            if v > best_val:
                best_val, best_child = v, child
    else:
        best_val, best_child = float("+inf"), None
        for child in env.sucesores(estado, "MIN"):
            v = etiquetas.get(child)
            if v is None:
                v = MiniMax(env, child, "MAX")
            if v < best_val:
                best_val, best_child = v, child

    if best_child is None:
        # No hay movimientos (terminal)
        return -1, estado, etiquetas.get(estado, 0.0)

    accion = _accion_desde(estado, best_child)
    return accion, best_child, best_val
