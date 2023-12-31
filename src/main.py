from Grafo import Graph
#from Mapa import fill_graph, heuristicaDistanciaLinhaReta #heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Menus import MenuPrincial
from Sistema import Sistema

def main():
    sistema = Sistema()
    sistema.grafo.load_json('mapa.json')
    #sistema.grafo.desenha()

    MenuPrincial(sistema)

if __name__ == "__main__":
    main()
