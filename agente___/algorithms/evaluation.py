
# agente___/algorithms/evaluation.py
from __future__ import annotations
from math import inf

WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),   # filas
    (0,3,6),(1,4,7),(2,5,8),   # columnas
    (0,4,8),(2,4,6),           # diagonales
]

def evaluate_tres_en_raya(estado: str, me: str = "X", opp: str = "O") -> float:
    """
    Heurística simple para 3-en-raya (X=MAX, O=MIN).
    +inf  si me gano, -inf si gana opp, 0 si empate terminal.
    En no terminales: cuenta líneas abiertas y 2-en-línea ponderadas.
    """
    # Terminales
    if _gana(estado, me):  return inf
    if _gana(estado, opp): return -inf
    if "." not in estado and not _gana(estado, me) and not _gana(estado, opp):
        return 0.0

    w2, w1 = 10.0, 1.0
    score = 0.0

    # Líneas
    for a,b,c in WIN_LINES:
        line = (estado[a], estado[b], estado[c])
        mc = line.count(me)
        oc = line.count(opp)
        if mc > 0 and oc == 0:
            score += w2 if mc == 2 else w1
        elif oc > 0 and mc == 0:
            score -= w2 if oc == 2 else w1

    # Centro
    if estado[4] == me:  score += 2.0
    if estado[4] == opp: score -= 2.0

    # Esquinas
    for i in (0,2,6,8):
        if estado[i] == me:  score += 1.0
        if estado[i] == opp: score -= 1.0

    return score

def _gana(estado: str, p: str) -> bool:
    for a,b,c in WIN_LINES:
        if estado[a] == estado[b] == estado[c] == p:
            return True
    return False
