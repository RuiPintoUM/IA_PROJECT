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

    def executaTrabalho(self, local1, local2, local3):
        pass

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
        estafeta.numClassificacoes += 1

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
        sorted_estafetas = sorted(self.mapEstafetas.values(), key=lambda estafeta: len(estafeta.encomenda_ids), reverse=True)
        top5_estafetas = sorted_estafetas[:5]
        print(f"Top 5 estafetas com mais entregas:")
        for i, estafeta in enumerate(top5_estafetas, 1):
            print(f"{i}. {estafeta.nome} - Entregas: {len(estafeta.encomenda_ids)}")

    #2 funções para o top5 de estafetas com mais entregas ecologicas
    def top_ranking_ecologicas(self):
        sorted_estafetas = sorted(self.mapEstafetas, key=lambda estafeta: self.conta_entregas_ecologicas(estafeta), reverse=True)
        top5_estafetas = sorted_estafetas[:5]
        print(f"Top 5 estafetas com mais entregas ecológicas(de bicicleta):")
        for i, estafeta in enumerate(top5_estafetas, 1):
            entregas_ecologicas = self.conta_entregas_ecologicas(estafeta)
            print(f"{i}. {estafeta.nome} - Entregas ecológicas: {entregas_ecologicas}")
            
    
    def conta_entregas_ecologicas(self, estafeta):
        entregas_ecologicas = 0
        for encomenda_id in estafeta.encomenda_ids:
            encomenda = self.mapEncomendas.get(encomenda_id)
            if encomenda and encomenda.veiculo == "Bicicleta":
                entregas_ecologicas += 1
        return entregas_ecologicas

    def top_ranking_rating(self):
        sorted_estafetas = sorted(self.mapEstafetas, key=lambda estafeta: estafeta.somaClassificacoes/estafeta.numClassificacoes, reverse=True)
        top5_estafetas = sorted_estafetas[:5]
        print(f"Top 5 estafetas com melhor média de classificações:")
        for i, estafeta in enumerate(top5_estafetas, 1):
            media_classificacoes = estafeta.somaClassificacoes/estafeta.numClassificacoes
            print(f"{i}. {estafeta.nome} - Média de Classificações: {media_classificacoes:.2f} ({estafeta.numClassificacoes} classificações)")
            
