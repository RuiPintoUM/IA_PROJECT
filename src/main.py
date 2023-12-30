from Grafo import Graph
from Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Menus import Menus
from Sistema import Sistema

def main():
    sistema = Sistema()
    sistema.iniciaEstafetas()

    Menus(sistema)

if __name__ == "__main__":
    main()
