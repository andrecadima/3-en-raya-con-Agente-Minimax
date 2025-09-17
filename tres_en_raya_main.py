from __future__ import annotations
from agente___.algorithms.minimax_simple import MiniMax
from agente___.agents.agente_tres_en_raya import mejor_jugada
from agente___.environments.tres_en_raya import EntornoTresEnRaya

def turno_actual(estado: str) -> str:
    # Si X y O tienen mismo conteo, le toca a X (MAX). Si no, a O (MIN).
    x = estado.count("X")
    o = estado.count("O")
    return "MAX" if x == o else "MIN"

def juego_humano_vs_ia():
    env = EntornoTresEnRaya()
    estado = "........."  # tablero vacío
    print("Comienza 3 en raya. MAX='X' (IA), MIN='O' (Humano).")
    print(env.render(estado), "\n")

    while not env.es_terminal(estado):
        jugador = turno_actual(estado)

        if jugador == "MAX":
            # IA (imbatible)
            accion, estado, valor = mejor_jugada(env, estado, "MAX")
            print(f"IA juega en {accion}. Valor esperado: {valor}")
            print(env.render(estado), "\n")

        else:
            # Humano
            libres = [i for i, c in enumerate(estado) if c == "."]
            while True:
                try:
                    jug = int(input(f"Tu turno (O). Elige posición {libres}: "))
                except Exception:
                    print("Entrada inválida.")
                    continue
                if jug in libres:
                    estado = estado[:jug] + "O" + estado[jug+1:]
                    break
                print("Casilla ocupada o fuera de rango.")
            print(env.render(estado), "\n")

    # Fin de la partida
    u = env.utilidad(estado)
    if u > 0:
        print("Gana la IA (X).")
    elif u < 0:
        print("¡Ganaste! (O)")
    else:
        print("Empate.")

if __name__ == "__main__":
    juego_humano_vs_ia()
