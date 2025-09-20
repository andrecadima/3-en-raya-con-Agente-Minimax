
from __future__ import annotations
from agente___.environments.tres_en_raya import EntornoTresEnRaya
from agente___.agents.agente_tres_en_raya_eval import mejor_jugada_eval
from agente___.algorithms.evaluation import evaluate_tres_en_raya

def main():
    env = EntornoTresEnRaya()
    estado = "........."  # tablero vacío
    turno = "MAX"  # IA = X

    print(env.render(estado), "\n")
    while not env.es_terminal(estado):
        if turno == "MAX":
            accion, estado, val = mejor_jugada_eval(env, estado, "MAX", depth=4)
            print(f"IA (X) juega en {accion} (eval={val:.2f})")
            print(env.render(estado), "\n")
            turno = "MIN"
        else:
            # Movimiento humano simple por input (0..8)
            mov = None
            while mov is None:
                try:
                    i = int(input("Tu jugada (0..8): "))
                    if 0 <= i <= 8 and estado[i] == ".":
                        s = list(estado)
                        s[i] = "O"
                        estado = "".join(s)
                        print(env.render(estado), "\n")
                        turno = "MAX"
                        mov = i
                    else:
                        print("Índice inválido o casilla ocupada.")
                except Exception:
                    print("Entrada inválida.")
    u = env.utilidad(estado)
    print("Resultado:", "Gana X" if u>0 else ("Gana O" if u<0 else "Empate"))

if __name__ == "__main__":
    main()
