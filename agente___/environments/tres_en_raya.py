from __future__ import annotations
from typing import List

# Representación:
# - Estado = str de longitud 9 con caracteres en {"X","O","."}
# - "." significa casilla vacía
#
# El algoritmo MiniMax que ya tienes espera:
#   sucesores(estado) -> List[estado_hijo]
#   es_terminal(estado) -> bool
#   utilidad(estado) -> float (visto por MAX='X')
#
# Aquí MAX = 'X' y MIN = 'O'

WIN_LINES = [
    (0,1,2), (3,4,5), (6,7,8),        # filas
    (0,3,6), (1,4,7), (2,5,8),        # columnas
    (0,4,8), (2,4,6)                  # diagonales
]

def _gana(estado: str, ficha: str) -> bool:
    return any(all(estado[i] == ficha for i in line) for line in WIN_LINES)

def _libres(estado: str) -> List[int]:
    return [i for i, c in enumerate(estado) if c == "."]

def _poner(estado: str, idx: int, ficha: str) -> str:
    # crea un nuevo estado con 'ficha' puesta en 'idx'
    return estado[:idx] + ficha + estado[idx+1:]

class EntornoTresEnRaya:
    """Entorno de 3 en raya compatible con MiniMax simple."""

    def sucesores(self, estado: str, jugador: str) -> List[str]:
        # jugador es "MAX" o "MIN"
        ficha = "X" if jugador == "MAX" else "O"
        if self.es_terminal(estado):
            return []
        return [_poner(estado, i, ficha) for i in _libres(estado)]

    def es_terminal(self, estado: str) -> bool:
        # Terminal si alguien ganó o no quedan casillas
        return _gana(estado, "X") or _gana(estado, "O") or ("." not in estado)

    def utilidad(self, estado: str) -> float:
        # Únicamente llamada en terminales.
        # +1 si gana X (MAX), -1 si gana O (MIN), 0 si empate.
        if _gana(estado, "X"):
            return 1.0
        if _gana(estado, "O"):
            return -1.0
        return 0.0

    # Helpers opcionales de visualización
    @staticmethod
    def render(estado: str) -> str:
        filas = [estado[0:3], estado[3:6], estado[6:9]]
        return "\n".join(" ".join(c if c != "." else "_" for c in f) for f in filas)
