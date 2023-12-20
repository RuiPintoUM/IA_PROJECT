from Grafo import Graph
from Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Encomenda import Encomenda
from Estafeta import Estafeta
import time

class Sistema:

    def __init__(self):     #  construtor do sistema"
        self.mapEstafetas = {}  # Dicionário para armazenar estafetas
        self.mapEncomendas = {}  # Dicionário para armazenar encomendas

    def iniciaEstafetas(self):
        estafeta1 = Estafeta(nome="Jefferson", status=1)
        estafeta2 = Estafeta(nome="Walson", status=1)
        estafeta3 = Estafeta(nome="Valter", status=0)
        estafeta4 = Estafeta(nome="Flipe", status=0)

        self.mapEstafetas = {
            1: estafeta1,
            2: estafeta2,
            3: estafeta3,
            4: estafeta4
        }

    def respostaPosEncomenda(self,encomenda, caminho):
        print("Caminho: ")
        for node in caminho:
            print(str(node))
        print(f"Encomenda demorou {encomenda.tempoReal} horas a ser entregue.")
        print(f"Encomenda foi entregue de {encomenda.veiculo}.")
        print(f"A distancia percorrida foi de {encomenda.distancia}km.")




    def removeEncomenda(self, encomenda):
        if encomenda.id in self.mapEncomendas:
            del self.mapEncomendas[encomenda.id]

        for estafeta in self.mapEstafetas.values():
            if encomenda.id in estafeta.encomenda_ids:
                estafeta.encomenda_ids.remove(encomenda.id)

    def criaEncomenda(self, local, peso, volume, tempoPedido, distancia):
        # Gera um novo ID para a encomenda
        if not self.mapEncomendas:
            id = 1
        else:
            id = max(self.mapEncomendas.keys()) + 1

        estafeta = self.atribuiEncomenda(id)

        enc = Encomenda(id, local, peso, volume, tempoPedido, estafeta, distancia)

        self.mapEncomendas[enc.id] = enc
        return enc

    def atribuiEncomenda(self, idEncomenda):

        print("À Procura do teu Estafeta.")

        time.sleep(1) #feature riso só para mostrar que tamos à procura dele

        for nome_estafeta, estafeta in self.mapEstafetas.items():
            if estafeta.status == 0:
                print("Estafeta encontrado.")
                print(estafeta.nome)
                estafeta.status = 1
                estafeta.addEncomenda(idEncomenda)
                return estafeta

        return "na"

    def calculaMelhorCaminho(self, g, local):
        (path1, custo1) = g.procura_BFS("lisboa", local)
        (path2, custo2) = g.procura_DFS("lisboa", local)
        #(path3, custo3) = g.procura_DFS("lisboa", local) #g.greedy("lisboa", local)
        #(path4, custo4) = g.procura_DFS("lisboa", local) #g.procura_aStar("lisboa", local)

        custoMin = (min(custo1, custo2))

        if custo1 == custoMin:
            melhorCaminho = path1
        elif custo2 == custoMin:
            melhorCaminho = path2
        #elif custo3 == custoMin:
        #    melhorCaminho = path3
        #else:
        #    melhorCaminho = path4

        return (melhorCaminho, custoMin)

    def adicionarEstafeta(self, nome_estafeta):
        estafeta = Estafeta(nome_estafeta)
        self.mapEstafetas[nome_estafeta] = estafeta






