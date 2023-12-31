from Grafo import Graph
#from Mapa import fill_graph, heuristicaDistanciaLinhaReta #heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Menus import MenuPrincial
from Sistema import Sistema

def main():
    sistema = Sistema()
    sistema.grafo.load_json('mapa.json')
    #istema.grafo.desenha()

    #MenuPrincial(sistema)

    sistema.calculaMelhorCaminho("Rua Gomes de Sa")

if __name__ == "__main__":
    main()
