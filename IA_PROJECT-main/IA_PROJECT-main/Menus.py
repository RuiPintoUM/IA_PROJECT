from Grafo import Graph
from Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Sistema import Sistema

def menuRankings(sitema):
    print("1 - Top 5 ranking estafetas com mais entregas efetuadas") # incluir posição atual do estafeta no ranking
    print("2 - Top 5 ranking estafetas com mais entregas ecológicas")
    print("3 - Top 5 ranking estafetas com melhor rating")
    print("4 - Sair")




def menuEncomendasEstafeta(sistema, nome):
    print(sistema.mostrarListaEncomendas(nome))
    print("--- Escolha o modo de entrega ---")
    print("1 - Caminho mais rápido")
    print("2 - Caminho mais ecológico")
    print("3 - Sair")


def menuEstafeta(sistema, nome):
    print("--- Menu Estafeta ---")
    print("1 - Verificar encomendas associadads")
    print("2 - Rankings")
    print("3 - Alterar Status")
    print("4 - Sair")

    user_input = int(input("Introduza a sua opcao-> "))

    match user_input:
        case 1:
            menuEncomendasEstafeta(sistema, nome)
        case 2:
            menuRankings(sistema)
        case 3:
            print("por fazer")
        case 4:
            menuEstafetaLogin(sistema)


def menuEstafetaLogin(sistema):
    print("--- Menu Login Estafeta ---")
    print("1 - Login")
    print("2 - Registar novo estafeta")
    print("3 - Sair")

    user_input = int(input("Introduza a sua opcao-> "))
    match user_input:
        case 1:
            nome_estafeta = input("Introduza o nome do estafeta-> ")
            if sistema.loginEstafeta(nome_estafeta):
                menuEstafeta(sistema, nome_estafeta)
            else:
                print("Estafeta não registado")
                menuEstafetaLogin(sistema)
        case 2:
            nome_estafeta = input("Introduza o nome do estafeta-> ")
            sistema.adicionarEstafeta(nome_estafeta)
        case 3:
            print("AGUEM ESCREVA AQUI O CÓDIGO, HUGO SECA NAO SABE FAZER MENUS") # -------------------------------------------------------------
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

            resultadoCaminho = sistema.calculaMelhorCaminho(g, local)

            if resultadoCaminho is None:
                print("O sistema não encontrou caminho para o local desejado.")
                l = input("prima enter para continuar")
            else:
                (caminho, distancia) = resultadoCaminho
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

                    avaliacao = input("digite a avaliacao do gajo (0 a 5): ")

                    sistema.atribuiAvaliacao(encomenda.estafeta, avaliacao)

                    input(f"Somaclassificaçoes: {encomenda.estafeta.somaClassificacoes}.")

                    input(f"A avaliação média de {encomenda.estafeta.nome} é {sistema.mediaEstafeta(encomenda.estafeta)}.")

                    sistema.removeEncomenda(encomenda)

            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")

        elif saida == 2:  # interface estafeta

            menuEstafetaLogin(sistema)

        else:

            print("you didn't add anything")
            print("\n\n\n\n\n\n")
            l = input("prima enter para continuar")

