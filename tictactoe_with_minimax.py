from agente___.algorithms.minimax_simple import MiniMax
from agente___.environments.entorno_grafo_especifico import EntornoGrafoEspecifico
from agente___.algorithms.minimax_simple import MiniMax as _mm

if __name__ == "__main__":
    adj = {
        "ROOT": ["A", "B", "C"],
        "A": ["A1", "A2", "A3"],
        "B": ["B1", "B2", "B3"],
        "C": ["C1", "C2", "C3"],
    }
    utilidad = {
        "A1": 3,  "A2": 12, "A3": 8,
        "B1": 2,  "B2": 4,  "B3": 6,
        "C1": 14, "C2": 5,  "C3": 2,
    }

    env = EntornoGrafoEspecifico(adj, utilidad)

    etiquetas = {}
    valor_root = MiniMax(env, "ROOT", "MAX", etiquetas)

    # Primera jugada óptima de MAX en ROOT
    mejor_accion = None
    mejor_valor = float("-inf")
    for hijo in env.sucesores("ROOT"):
        v_hijo = etiquetas.get(hijo)
        if v_hijo is None:
            # por si no se etiquetó (normalmente ya estará)
            v_hijo = _mm(env, hijo, "MIN")
        if v_hijo > mejor_valor:
            mejor_valor, mejor_accion = v_hijo, hijo

    print("Valor en ROOT:", valor_root)                
    print("Primera jugada de MAX:", mejor_accion)      
    print("Valor de esa jugada:", mejor_valor)         
