from Grafo import Graph
from Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Encomenda import Encomenda
from Estafeta import Estafeta
import time

class Sistema:

    def __init__(self):     #  construtor do sistema"
        self.mapEstafetas = {}  # Dicionário para armazenar estafetas
        self.mapEncomendas = {}  # Dicionário para armazenar encomendas

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

        encomenda.estafeta.status = 0

    def criaEncomenda(self, local, peso, volume, tempoPedido, distancia):
        # Gera um novo ID para a encomenda
        if not self.mapEncomendas:
            id = 1
        else:
            id = max(self.mapEncomendas.keys()) + 1

        #estafeta = self.atribuiEncomenda(id)

        enc = Encomenda(id, local, peso, volume, tempoPedido, distancia)

        if enc.tempoReal != "na":
            enc.estafeta = self.atribuiEncomenda(id)

        self.mapEncomendas[enc.id] = enc
        return enc

    def atribuiEncomenda(self, idEncomenda):

        print("À Procura do teu Estafeta.")

        time.sleep(1) #feature riso só para mostrar que tamos à procura dele

        for nome_estafeta, estafeta in self.mapEstafetas.items():
            if estafeta.status == 0:
                print("Encontramos o teu Estafeta")
                print(estafeta.nome)
                estafeta.status = 1
                estafeta.addEncomenda(idEncomenda)
                return estafeta

        return "na"

    def atribuiAvaliacao(self, estafeta, avaliacao):
        estafeta.somaClassificacoes += int(avaliacao)

    def mediaEstafeta(self, estafeta):
        return  estafeta.somaClassificacoes / len(estafeta.encomenda_ids)

    def calculaMelhorCaminho(self, g, local):

        result_BFS = g.procura_BFS("lisboa", local)
        result_DFS = g.procura_DFS("lisboa", local)


        if result_BFS and result_DFS is None: return None
        elif result_BFS is not None and result_DFS is None:
            (path1, custo1) = result_BFS
            return (path1, custo1)
        elif result_DFS is not None and result_BFS is None:
            (path2, custo2) = result_DFS
            return (path2, custo2)
        else:
            (path1, custo1) = result_BFS
            (path2, custo2) = result_DFS
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

    def adicionarEstafeta(self, nome_estafeta, status):
        estafeta = Estafeta(nome_estafeta, status)
        self.mapEstafetas[nome_estafeta] = estafeta

    def loginEstafeta(self, nome):
        if nome in self.mapEstafetas:
            return True
        else:
            return False
        
    def mostrarListaEncomendas(self, nome):
        estafeta = self.mapEstafetas.get(nome)
        
        return estafeta.getEncomendas()


    def iniciaEstafetas(self):
        self.adicionarEstafeta("Jefferson", 1)
        self.adicionarEstafeta("Walson", 1)
        self.adicionarEstafeta("Valter", 0)
        self.adicionarEstafeta("Flipe", 0)

    # --- Queries ---

    def top_ranking_entregas(self):
        sorted_estafetas = sorted(self.estafetas.items(), key=estafeta.encomenda_ids.len , reverse=True)
        print(f"Top 5 estafetas com mais entregas efetuadas:")
        for i, (estafeta, dados) in enumerate(sorted_estafetas[:5], 1):
            print(f"{i}. {estafeta} - Entregas: {dados['entregas']}")

    def top_ranking_ecologicas(self, n=5):
        sorted_estafetas = sorted(self.estafetas.items(), key=lambda x: x[1]['entregas_ecologicas'], reverse=True)
        print(f"Top {n} estafetas com mais entregas ecológicas:")
        for i, (estafeta, dados) in enumerate(sorted_estafetas[:n], start=1):
            print(f"{i}. {estafeta} - Entregas Ecológicas: {dados['entregas_ecologicas']}")

    def top_ranking_rating(self, n=5):
        sorted_estafetas = sorted(self.estafetas.items(), key=lambda x: x[1]['rating'], reverse=True)
        print(f"Top {n} estafetas com melhor rating:")
        for i, (estafeta, dados) in enumerate(sorted_estafetas[:n], start=1):
            print(f"{i}. {estafeta} - Rating: {dados['rating']}")
