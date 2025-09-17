# AGENTE 3 EN RAYA (USING MINIMAX)

Proyecto mínimo para un **Agente de 3 en raya (TicTacToe)** que usa el algoritmo **MINIMAX**.  
El agente **MAX = 'X'** nunca pierde: siempre gana o, en el peor de los casos, empata.

---

## Estructura del proyecto

3-en-raya-con-Agente-Minimax/
│
├─ agente___/ # Paquete principal (recuerda init.py)
│ ├─ algorithms/ # Algoritmos de búsqueda (minimax_simple.py, etc.)
│ ├─ agents/ # Agentes específicos (ej. agente_tres_en_raya.py)
│ ├─ environments/ # Entornos de juego (ej. tres_en_raya.py, entorno_grafo_especifico.py)
│ └─ init.py
│
├─ tres_en_raya_main.py # Script principal para jugar humano vs IA
├─ README.md
└─ requirements.txt # Dependencias (opcional)


---

## Uso

Ejecuta el script principal desde la raíz del proyecto:

```bash
python tres_en_raya_main.py

El juego comenzará en consola:

El agente IA (X) juega primero.

El humano (O) introduce movimientos indicando el índice de la casilla (0–8).

El tablero se muestra como una cuadrícula 3x3 en cada turno.

Ejemplo de inicio:

Comienza 3 en raya. MAX='X' (IA), MIN='O' (Humano).
_ _ _
_ _ _
_ _ _

IA juega en 0. Valor esperado: 0
X _ _
_ _ _
_ _ _

Índices de casillas

Para introducir movimientos, las posiciones del tablero se numeran así:

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8

Notas

La implementación de MiniMax está desacoplada del entorno:
funciona tanto con un grafo de ejemplo (EntornoGrafoEspecifico) como con el entorno de 3 en raya (EntornoTresEnRaya).

El código está listo para extender con poda Alpha-Beta o heurísticas si se quiere escalar a juegos más grandes.