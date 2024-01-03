from Grafo import Graph
#from Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Sistema import Sistema

def MenuPrincipal(sistema):
    opcao = -1
    while True:
        print("\n--- Menu Principal ---\n")
        print("1 - Interface Cliente")
        print("2 - Interface Estafeta")
        print("3 - Interface Admnistrador")
        print("4 - Guardar estado")
        print("0 - Sair")

        opcao = int(input("Introduza a sua opcao - "))

        match opcao:
            case 0:
                print("Saindo.......")
                break

            case 1:  # interface cliente
                menuClienteLogin(sistema)

            case 2:  # interface estafeta
                menuEstafetaLogin(sistema)

            case 3:  # interface admnistrador
                menuAdmin(sistema)

            case 4:  # save
                sistema.guardarData()

            case _:
                print("Opção inválida")


def menuClienteLogin(sistema):
        print("\n--- Menu Login Cliente ---\n")
        print("1 - Login")
        print("2 - Registar Cliente")
        print("0 - Voltar")

        opcao = int(input("Introduza a sua opcao - "))

        match opcao:
            case 0:
                MenuPrincipal(sistema)

            case 1:  # login
                nome_cliente = input("Introduza o nome do cliente-> ")
                if sistema.loginCliente(nome_cliente):
                    menuCliente(sistema, nome_cliente)
                else:
                    print("Cliente não registado")

            case 2:  
                nome_cliente = input("Introduza o seu nome: ")

                sistema.adicionarCliente(nome_cliente)
                print("Registro completo")

                menuClienteLogin(sistema)
            case _:
                print("Opção inválida")

def menuCliente(sistema, nome):
    print("\n--- Menu Login Estafeta ---\n")
    print("1 - Fazer encomenda")
    print("2 - Avaliar Estafetas que fizeram entrega")
    print("0 - Voltar")

    opcao = int(input("Introduza a sua opcao - "))

    match opcao:
        case 0:
            menuClienteLogin(sistema)

        case 1:  
            menuClienteFazerEncomenda(sistema, nome)

        case 2:  
            menuAvaliarEstafetas(sistema, nome)

        case _:
            print("Opção inválida")


def menuAvaliarEstafetas(sistema, nome):
    estafetas = sistema.getEstafetasParaAvaliar(nome)
    i = 1

    print("--- Estafetas para Avaliar ---")
    if(len(estafetas) == 0):
        print("-> Não há estafetas para avaliar!")
    else:
        for estafeta in estafetas:
            print(f"{i} -> {estafeta[1].nome} da encomenda de id {estafeta[0]}")
            i += 1
    print("\n0 -> Voltar")
    opcao = int(input("Introduza a sua opcao - "))

    if opcao == 0:
        menuCliente(sistema, nome)
    elif 1 <= opcao <= i:
        aval = int(input("Avalie de 0 a 5 - "))
        cliente = sistema.clientes[nome]
        cliente.removeEstafetaParaAva(estafetas[opcao-1][0])
        sistema.atribuiAvaliacao(estafetas[opcao-1][1], aval)

        menuAvaliarEstafetas(sistema, nome)
    else:
        print("Opção inválida")


def menuClienteFazerEncomenda(sistema, nome):
    print("\n--- Menu Cliente ---")

    while (peso := float(input("\nPeso da Encomenda: "))) > 100 or peso <= 0:
        print("Peso não suportado.")

    while (volume := float(input("\nVolume da Encomenda: "))) <= 0:
        print("Volume inválido.")

    while (tempoPedido := float(input("\nTempo em que quer receber a Encomenda (0 se não tiver preferência): "))) < 0:
        print("Tempo inválido.")

    while not sistema.localidadeExiste(local := input("\nLocal onde deseja receber a Encomenda: ")):
        print(f"O local '{local}' não existe.")

    distancia = sistema.calculaMelhorCaminho(local, "bestpath")[1]

    estafeta = sistema.estafetaMaisEcologico(peso, distancia, tempoPedido)

    if estafeta == None:
        print("Prazo de entrega é muito curto para a localidade que escolheu")
        menuClienteLogin(sistema)

    if (input(f"O preço da encomenda é {sistema.definePreco(estafeta.veiculo, volume, distancia, tempoPedido)}. Deseja aceitar? (S ou N): ").lower() == "s"):
        enc = sistema.novaEncomenda(local, peso, volume, tempoPedido, distancia, nome)
        estafeta.adicionaEnc(enc.id)
    else:
        MenuPrincipal(sistema)

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
    print("0 - Sair")

    user_input = int(input("Introduza a sua opcao - "))

    match user_input:
        case 1:
            menuEncomendasEstafeta(sistema, nome)
        case 2:
            menuRankings(sistema, nome)
        case 3:
            print("por fazer")
        case 4:
            pass
        case 0:
            menuEstafetaLogin(sistema)

def extractIdsLocalsString(encomendasString):
    idsLocalsString = {}
    
    # Encontrar todas as ocorrências de "ID: "
    indexIds = [index for index, palavra in enumerate(encomendasString.split()) if palavra == "ID:"]

    for indexId in indexIds:
        encIdString = encomendasString.split()[indexId + 1].replace(',', '')  # Remover vírgula
        encId = int(encIdString)
        local_index = encomendasString.find("Local de Entrega:", indexId)
        local = encomendasString[local_index:].split(": ")[1].split("\n")[0]
        idsLocalsString[encId] = local

    return idsLocalsString

def menuEncomendasEstafeta(sistema, nome):
    print("--- Encomendas para Entrega diponíveis ---")
    encomendasString = sistema.mostrarEncomendasEstafetas(nome)

    idsLocalsString = extractIdsLocalsString(encomendasString)

    user_input = int(input("\nIntroduza o ID da Encomenda - "))
    
    if user_input in idsLocalsString:
        local = idsLocalsString[user_input]
        
        (caminho, custo) = sistema.calculaMelhorCaminho(local, "transit")
        sistema.respostaPosEncomenda(user_input, nome, caminho)

        sistema.removeEncomenda(user_input, nome)

        menuEstafeta(sistema, nome)
    else:
        print("ID da encomenda não válido. Tente novamente.")
        menuEncomendasEstafeta(sistema, nome)
    
def menuRankings(sistema, nome):
    print("1 - Top 5 ranking estafetas com melhor avaliação média") 
    print("2 - Top 5 ranking de estafetas com mais entregas feitas")
    print("3 - Top 5 ranking de estafetas com mais entregas de carro feitas")
    print("4 - Top 5 ranking de estafetas com mais entregas de mota feitas")
    print("5 - Top 5 ranking de estafetas com mais entregas de bicicleta feitas")
    print("0 - Sair")

    user_input = int(input("Introduza a sua opcao-> "))
    match user_input:
        case 1:
            sistema.rankingNumEntregasGeral(nome)
            menuRankings(sistema, nome)
        case 2:
            sistema.rankingNumEntregasGeral(nome)
            menuRankings(sistema, nome)
        case 3:
            sistema.rankingNumEntregasCarro(nome)
            menuRankings(sistema, nome)
        case 4:
            sistema.rankingNumEntregasMota(nome)
            menuRankings(sistema, nome)
        case 5:
            sistema.rankingNumEntregasBicicleta(nome)
            menuRankings(sistema, nome)           
        case 0:
            menuEstafeta(sistema, nome)
        
def menuAdmin(sistema):
    opcao = -1
    while True: 
        print("\n--- Menu Administrador ---\n")
        print("1 - Mostrar Encomendas")
        print("2 - Mostrar Estafetas")
        print("0 - Voltar")
        
        opcao = int(input("Introduza a sua opcao - "))

        match opcao:
            case 0:
                break

            case 1:  # Mostrar Encomendas (reutilizar a função encomendas disponíveis)
                print(f"\n--- Entregas ---\n{sistema.mostraEncomendasAdmin()}")

            case 2:  # Mostrar Estafetas
                print(f"\n--- Estafetas ---\n{sistema.mostrarEstafetasAdmin()}")

            case _:
                print("Opção inválida")
