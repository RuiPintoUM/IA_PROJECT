from typing import Any

from Grafo import Graph
from Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Sistema import Sistema


class Menus:
    g = Graph()
    fill_graph(g)
    sistema = Sistema()

    saida = 1

    while saida != 0:
        print("1 - Interface Cliente")
        print("2 - Interface Estafeta")
        print("0 - Sair")

        saida = int(input("introduza a sua opcao-> "))

        if saida == 0:

            print("\n\n\n\n\n\n")
            print("saindo.......")

        elif saida == 1:  # interface cliente

            sistema.iniciaEstafetas()

            peso = input("Peso da Encomenda: ")
            volume = input("Volume da Encomenda: ")
            tempoPedido = input("Tempo em que quer receber a Encomenda (0 se não tiver preferência): ")
            local = input("Local onde deseja receber a Encomenda: ")

            (caminho, distancia) = sistema.calculaMelhorCaminho(g, local)

            encomenda = sistema.criaEncomenda(local, peso, volume, tempoPedido, distancia)

            if encomenda.veiculo == "na":
                print("Encomenda não pode ser entregue no tempo pedido.")
            elif encomenda.estafeta == "na":
                print("Não há estafetas disponíveis no momento.")
            else:
                confirmacao = input(f"O preço da encomenda é {encomenda.preco}. Deseja aceitar? (S ou N): ")

                if confirmacao == "S".lower():
                    pass
                else:
                    sistema.removeEncomenda(encomenda)
                    l = input("prima enter para voltar atrás")
                    # chamar menu de saida

            print("...Encomenda a ser feita no momento...")

            sistema.respostaPosEncomenda(encomenda, caminho)
            sistema.removeEncomenda(encomenda)

            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")

        elif saida == 2:  # interface estafeta

            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")

        else:

            print("you didn't add anything")
            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")
