
from __future__ import annotations
from agente___.environments.tres_en_raya_nxn import EntornoTresEnRayaNxN
from agente___.agents.agente_tres_en_raya_nxn import mejor_jugada_nxn

def main():
    n = 5
    win_k = 5   # puedes cambiar a 3 o 5 según el desafío
    env = EntornoTresEnRayaNxN(n=n, win_k=win_k)
    estado = "." * (n * n)
    turno = "MAX"  # IA empieza (X)

    print(env.render(estado), "\n")
    while not env.es_terminal(estado):
        if turno == "MAX":
            # depth=4-6 suele ir bien en 5x5. Sube/baja según rendimiento.
            accion, estado, val = mejor_jugada_nxn(env, estado, "MAX", depth=5)
            print(f"IA (X) juega en {accion} (eval={val:.2f})")
            print(env.render(estado), "\n")
            turno = "MIN"
        else:
            # Humano
            mov = None
            while mov is None:
                try:
                    i = int(input(f"Tu jugada (0..{n*n-1}): "))
                    if 0 <= i < n*n and estado[i] == ".":
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
