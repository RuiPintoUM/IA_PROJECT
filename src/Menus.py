from Grafo import Graph
#from Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Sistema import Sistema

def MenuPrincial(sistema):
    opcao = -1
    while True:
        print("\n--- Menu Principal ---\n")
        print("1 - Interface Cliente")
        print("2 - Interface Estafeta")
        print("3 - Interface Admnistrador")
        print("0 - Sair")

        opcao = int(input("Introduza a sua opcao - "))

        match opcao:
            case 0:
                print("Saindo.......")
                break

            case 1:  # interface cliente
                menuCliente(sistema)

            case 2:  # interface estafeta
                menuEstafetaLogin(sistema)

            case 3:  # interface admnistrador
                pass

            case _:
                print("Opção inválida")

def menuCliente(sistema):
    print("\n--- Menu Cliente ---")

    while (peso := float(input("\nPeso da Encomenda: "))) > 100 or peso <= 0:
        print("Peso não suportado.")

    while (volume := float(input("\nVolume da Encomenda: "))) <= 0:
        print("Volume inválido.")

    while (tempoPedido := float(input("\nTempo em que quer receber a Encomenda (0 se não tiver preferência): "))) < 0:
        print("Tempo inválido.")

    while not sistema.localidadeExiste(local := input("\nLocal onde deseja receber a Encomenda: ")):
        print(f"O local '{local}' não existe.")

    distancia = sistema.calculaMelhorCaminho(local)[1]
    sistema.novaEncomenda(local, peso, volume, tempoPedido, distancia)
    '''
    if resultadoCaminho is None:
        print("O sistema não encontrou caminho para o local desejado.")
        MenuPrincial(sistema)
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
                Menus(sistema)

            print("...Encomenda a ser feita no momento...")
            sistema.respostaPosEncomenda(encomenda, caminho)
            avaliacao = input("Digite a avaliacao do gajo (0 a 5): ")
            sistema.atribuiAvaliacao(encomenda.estafeta, avaliacao)
            print(f"Somaclassificaçoes: {encomenda.estafeta.somaClassificacoes}.")
            print(f"A avaliação média de {encomenda.estafeta.nome} é {sistema.mediaEstafeta(encomenda.estafeta)}.")

    '''

def menuEstafetaLogin(sistema):
    opcao = -1
    while True:
        print("\n--- Menu Login Estafeta ---\n")
        print("1 - Login")
        print("2 - Registar novo estafeta")
        print("0 - Voltar")

        opcao = int(input("Introduza a sua opcao - "))

        match opcao:
            case 0:
                break

            case 1:  # login
                nome_estafeta = input("Introduza o nome do estafeta-> ")
                if sistema.loginEstafeta(nome_estafeta):
                    menuEstafeta(sistema, nome_estafeta)
                else:
                    print("Estafeta não registado")

            case 2:  # registro
                nome_estafeta = input("Introduza o seu nome: ")

                while not (veiculo := input("Qual é o seu veiculo (bicicleta/mota/carro): ").lower()) in ["bicicleta","mota","carro"]:
                    print("Veiculo inválido.")
                sistema.adicionarEstafeta(nome_estafeta, 0, veiculo)
                print("Registro completo")

            case _:
                print("Opção inválida")

def menuEstafeta(sistema, nome):
    print("\n--- Menu Estafeta ---\n")
    print("1 - Verificar encomendas disponíveis")
    print("2 - Rankings")
    print("3 - Alterar Status")
    print("4 - Trabalhos para Efetuar")
    print("5 - Sair")

    user_input = int(input("Introduza a sua opcao-> "))

    match user_input:
        case 1:
            menuEncomendasEstafeta(sistema, nome)
        case 2:
            menuRankings(sistema, nome)
        case 3:
            print("por fazer")
        case 4:
            menuTrabalhos(sistema)
        case 5:
            menuEstafetaLogin(sistema)

    
def menuRankings(sistema, nome):
    print("1 - Top 5 ranking estafetas com mais entregas efetuadas") # incluir posição atual do estafeta no ranking
    print("2 - Top 5 ranking estafetas com mais entregas ecológicas")
    print("3 - Top 5 ranking estafetas com melhor rating")
    print("4 - Sair")

    user_input = int(input("Introduza a sua opcao-> "))
    match user_input:
        case 1:
            print()
        case 2:
            print()
        case 3:
            print()
        case 4:
            print(menuEstafeta(sistema, nome))

def menuEncomendasEstafeta(sistema, nome):
    encomendasDisponivies = Sistema.mostrarEncomendasDisponiveis(nome)

    print("--- Entregas diponíveis ---")
    print(encomendasDisponivies)
    print("--- Escolha o modo de entrega ---")

    print("1 - Adicionar uma encomenda")
    print("2 - Caminho mais ecológico")
    print("3 - Sair")

    user_input = int(input("Introduza a sua opcao-> "))
    match user_input:
        case 1:
            print()
        case 2:
            print()
        case 3:
            print(menuEstafeta(sistema, nome))

def menuTrabalhos(sistema):
    print("\n--- Menu Trabalhos ---\n")
    print(" 1 - Trabalho 1")
    print("     Encomenda para entregar em Elvas")
    print("     Encomenda para entregar em Montemor")
    print("     Encomenda para entregar em Estremoz")
    print(" 2 - Trabalho 2")
    print("     Encomenda para entregar em Vendasnovas")
    print("     Encomenda para entregar em Redondo")
    print("     Encomenda para entregar em Moita")
    print(" 3 - Trabalho 3")
    print("     Encomenda para entregar em Arraiolos")
    print("     Encomenda para entregar em Borba")
    print("     Encomenda para entregar em Palmela")

    user_input = int(input("Introduza a sua opcao - "))

    match user_input:
        case 1:
            sistema.executaTrabalho("elvas", "montemor", "estremoz")
        case 2:
            sistema.executaTrabalho("vendasnovas", "redondo", "moita")
        case 3:
            sistema.executaTrabalho("arraiolos", "borba", "palmela")