from Grafo.Grafo import Graph
from Grafo.Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito

def main():

    g = Graph()
    fill_graph(g)

    saida = -1
    while saida != 0:
        print("1-Imprimir Grafo")
        print("2-Desenhar Grafo")
        print("3-Imprimir  nodos de Grafo")
        print("4-Imprimir arestas de Grafo")
        print("5-Pesquisa não Informada")
        print("6-Pesquisa Informada")
        print("0-Saír")

        saida = int(input("introduza a sua opcao-> "))
        if saida == 0:
            print("\n\n\n\n\n\n")
            print("saindo.......")
        elif saida == 1:
            print(g.m_graph)
            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")
        elif saida == 2:
            g.desenha()
        elif saida == 3:
            print(g.m_graph.keys())
            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")
        elif saida == 4:
            print(g.imprime_aresta())
            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")
        elif saida == 5:
            print("1-DFS")
            print("2-BFS")
            saida = int(input("introduza a sua opcao-> "))
            while(saida == 1 or saida == 2):
                if saida == 1:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print(g.procura_DFS(inicio, fim, path=[], visited=set()))
                    print("\n\n\n\n\n\n")
                    l = input("prima enter para continuar")
                elif saida == 2:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print(g.procura_BFS(inicio, fim))
                    print("\n\n\n\n\n\n")
                    l = input("prima enter para continuar")
        elif saida == 6:
            print("1 - Preferência por média de combustivel gasto nas cidades.")
            print("2 - Preferência por cidades com menos temporais.")
            print("3 - Preferência por menos trânsito.")
            print("4 - A*")
            print("5 - Gulosa")

            saida = int(input("introduza a sua opcao-> "))

            while (saida == 1 or saida == 2 or saida == 3 or saida == 4 or saida == 5):
                if saida == 1:
                    print(heuristicaCombustivel(g))
                    print("\n\n\n\n\n\n")
                    l = input("prima enter para continuar")
                if saida == 2:
                    print(heuristicaTemporais(g))
                    print("\n\n\n\n\n\n")
                    l = input("prima enter para continuar")
                if saida == 3:
                    print(heuristicaTransito(g))
                    print("\n\n\n\n\n\n")
                    l = input("prima enter para continuar")
                elif saida == 4:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print(g.procura_aStar(inicio, fim))
                    print("\n\n\n\n\n\n")
                    l = input("prima enter para continuar")
                elif saida == 5:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print(g.greedy(inicio, fim))
                    print("\n\n\n\n\n\n")
                    l = input("prima enter para continuar")
        else:
            print("you didn't add anything")
            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")


if __name__ == "__main__":
    main()
