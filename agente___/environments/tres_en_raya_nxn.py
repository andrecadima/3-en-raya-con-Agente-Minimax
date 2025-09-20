
from __future__ import annotations
from typing import List, Tuple

class EntornoTresEnRayaNxN:
    """
    Estado = str de longitud n*n con caracteres en {"X","O","."}
    MAX = 'X', MIN = 'O'
    Ganar = conectar win_k en línea (horizontal, vertical, diagonal).
    """
    def __init__(self, n: int = 3, win_k: int = 3):
        assert n >= 3, "n debe ser >= 3"
        assert 3 <= win_k <= n, "win_k debe estar entre 3 y n"
        self.n = n
        self.win_k = win_k

    # ---- API esperada por MiniMax ----
    def sucesores(self, estado: str, jugador: str) -> List[str]:
        ficha = "X" if jugador == "MAX" else "O"
        hijos: List[str] = []
        for i, c in enumerate(estado):
            if c == ".":
                s = list(estado)
                s[i] = ficha
                hijos.append("".join(s))
        return hijos

    def es_terminal(self, estado: str) -> bool:
        return self._gana(estado, "X") or self._gana(estado, "O") or "." not in estado

    def utilidad(self, estado: str) -> float:
        if self._gana(estado, "X"): return 1.0
        if self._gana(estado, "O"): return -1.0
        return 0.0

    # ---- Lógica de victoria ----
    def _gana(self, estado: str, p: str) -> bool:
        n, k = self.n, self.win_k
        grid = [estado[i*n:(i+1)*n] for i in range(n)]
        # Horizontal y vertical
        for r in range(n):
            for c in range(n-k+1):
                if all(grid[r][c+j] == p for j in range(k)): return True
        for c in range(n):
            for r in range(n-k+1):
                if all(grid[r+j][c] == p for j in range(k)): return True
        # Diagonal principal
        for r in range(n-k+1):
            for c in range(n-k+1):
                if all(grid[r+j][c+j] == p for j in range(k)): return True
        # Diagonal secundaria
        for r in range(n-k+1):
            for c in range(k-1, n):
                if all(grid[r+j][c-j] == p for j in range(k)): return True
        return False

    # ---- Render bonito ----
    def render(self, estado: str) -> str:
        n = self.n
        filas = [estado[i*n:(i+1)*n] for i in range(n)]
        return "\n".join(" ".join(c if c != '.' else '_' for c in fila) for fila in filas)
