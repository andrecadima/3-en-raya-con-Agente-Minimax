# agente___/algorithms/minimax_simple.py
from __future__ import annotations
from typing import Dict, List, Optional, Literal, Protocol, Any, Iterable

Jugador = Literal["MAX", "MIN"]

class EntornoMinimax(Protocol):
    def es_terminal(self, estado: Any) -> bool: ...
    def utilidad(self, estado: Any) -> float: ...
    # Nota: algunos entornos definen sucesores(estado, jugador) y otros sucesores(estado)
    # Nosotros soportaremos ambos.

def _sucesores(env: Any, estado: Any, jugador: Jugador) -> Iterable[Any]:
    """
    Intenta llamar env.sucesores con (estado, jugador). Si el entorno
    acepta solo (estado), lo usamos sin el jugador.
    """
    try:
        return env.sucesores(estado, jugador)  # entornos tipo TresEnRaya
    except TypeError:
        return env.sucesores(estado)           # entornos tipo GrafoEspecifico

def MiniMax(env: EntornoMinimax, estado: Any, jugador: Jugador,
            etiquetas: Optional[Dict[Any, float]] = None) -> float:
    if env.es_terminal(estado):
        v = env.utilidad(estado)
        if etiquetas is not None:
            etiquetas[estado] = v
        return v

    if jugador == "MAX":
        v = valorMax(env, estado, etiquetas)
    else:
        v = valorMin(env, estado, etiquetas)

    if etiquetas is not None:
        etiquetas[estado] = v
    return v

def valorMax(env: EntornoMinimax, estado: Any,
             etiquetas: Optional[Dict[Any, float]] = None) -> float:
    v = float("-inf")
    for hijo in _sucesores(env, estado, "MAX"):
        v = max(v, MiniMax(env, hijo, "MIN", etiquetas))
    return v

def valorMin(env: EntornoMinimax, estado: Any,
             etiquetas: Optional[Dict[Any, float]] = None) -> float:
    v = float("+inf")
    for hijo in _sucesores(env, estado, "MIN"):
        v = min(v, MiniMax(env, hijo, "MAX", etiquetas))
    return v
