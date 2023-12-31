import json
import os
from Grafo import Graph
#from Mapa import fill_graph, heuristicaCombustivel, heuristicaTemporais, heuristicaTransito
from Encomenda import Encomenda
from Estafeta import Estafeta
import time

class Sistema:

    def __init__(self):     #  construtor do sistema"
        self.mapEstafetas = {}  # Dicionário para armazenar estafetas
        self.listaEncomendas = []  # Dicionário para armazenar encomendas
        self.grafo = Graph()
        self.carregaData()

    def localidadeExiste(self, nome):
        return self.grafo.locationExists(nome)
    
    def novaEncomenda(self, local, peso, volume, tempoPedido, distancia):
        enc = Encomenda(local, peso, volume, tempoPedido, distancia)
        self.listaEncomendas.append(enc)

    def adicionarEstafeta(self, nome_estafeta, status, veiculo):
        estafeta = Estafeta(nome_estafeta, status, veiculo)
        self.mapEstafetas[nome_estafeta] = estafeta

    def guardarData(self):
        map_path = os.path.join('data', 'estafetas.json')
        existing_data = []

        for estafeta in self.mapEstafetas.values():
            new_estafeta_data = {
                "nome": estafeta.nome,
                "status": estafeta.status,
                "veiculo": estafeta.veiculo,
                "listaEnc": estafeta.listaEncomenda,
                "somaClass": estafeta.somaClassificacoes
            }
            existing_data.append(new_estafeta_data)

        with open(map_path, 'w') as file:
            json.dump(existing_data, file, indent=2)

        encomendas_path = os.path.join('data', 'encomendas.json')
        existing_data = []

        for encomenda in self.listaEncomendas:
            new_encomenda_data = {
                "local": encomenda.localChegada,
                "peso": encomenda.peso,
                "volume": encomenda.volume,
                "tempo": encomenda.tempoPedido,
                "dist": encomenda.distancia
            }
            existing_data.append(new_encomenda_data)

        with open(encomendas_path, 'w') as file:
            json.dump(existing_data, file, indent=2)

    def carregaData(self):
        estafetas_path = os.path.join('data', 'estafetas.json')
        encomendas_path = os.path.join('data', 'encomendas.json')

        with open(estafetas_path, 'r') as estafetas_file:
            estafetas_data = json.load(estafetas_file)

            for estafeta_data in estafetas_data:
                estafeta = Estafeta(
                    nome=estafeta_data["nome"],
                    status=estafeta_data["status"],
                    veiculo=estafeta_data["veiculo"],
                    listaEncomenda=estafeta_data["listaEnc"],
                    somaClassificacoes=estafeta_data["somaClass"]
                )
                self.mapEstafetas[estafeta_data["nome"]] = estafeta

        with open(encomendas_path, 'r') as encomendas_file:
            encomendas_data = json.load(encomendas_file)

            for encomenda_data in encomendas_data:
                encomenda = Encomenda(
                    localChegada=encomenda_data["local"],
                    peso=encomenda_data["peso"],
                    volume=encomenda_data["volume"],
                    tempoPedido=encomenda_data["tempo"],
                    distancia=encomenda_data["dist"]
                )
                self.listaEncomendas.append(encomenda)

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

    def printanomes(self):
        for estafeta_id, estafeta in self.mapEstafetas.items():
            print(estafeta.nome)

    def executaTrabalho(self, local1, local2, local3):
        pass

    def mostrarEncomendasDisponiveis(self, nome):
        estafeta = self.mapEstafetas.get(nome)

        listaEncomendas = []

        for encomenda in self.mapEncomendas():
            if estafeta.verificaAddEncomenda():
                listaEncomendas.add(encomenda)

        return listaEncomendas

    def atribuiEncomenda(self, idEncomenda):

        print("À Procura do teu Estafeta.")

        time.sleep(1) #feature riso só para mostrar que tamos à procura dele

        for nome_estafeta, estafeta in self.mapEstafetas.items():
            if estafeta.status == 0:  # sistema saber que estafeta ainda é capaz de ter mais encomendas
                print("Encontramos o teu Estafeta")
                print(estafeta.nome)
                estafeta.status = 1
                estafeta.addEncomenda(idEncomenda)
                return estafeta

        return "na"

    def atribuiAvaliacao(self, estafeta, avaliacao):
        estafeta.somaClassificacoes += int(avaliacao)
        estafeta.status = 0

    def mediaEstafeta(self, estafeta):
        print(estafeta.somaClassificacoes)
        print("/")
        print(len(estafeta.encomenda_ids))
        return estafeta.somaClassificacoes / len(estafeta.encomenda_ids)

    def calculaMelhorCaminho(self, local):
        result_BFS = self.grafo.procura_BFS("Central", local)
        result_DFS = self.grafo.procura_DFS("Central", local)

        if result_BFS is None and result_DFS is None:
            return None
        elif result_BFS is not None and result_DFS is None:
            (path1, custo1) = result_BFS
            return (path1, custo1)
        elif result_DFS is not None and result_BFS is None:
            (path2, custo2) = result_DFS
            return (path2, custo2)
        else:
            (path1, custo1) = result_BFS
            (path2, custo2) = result_DFS

            custoMin = min(custo1, custo2)

            if custo1 == custoMin:
                melhorCaminho = path1
            elif custo2 == custoMin:
                melhorCaminho = path2

            print("Melhor Caminho:", melhorCaminho)
            print("Custo Mínimo:", custoMin)

            return (melhorCaminho, custoMin)

    def adicionarEstafeta(self, nome_estafeta, status, veiculo):
        estafeta = Estafeta(nome_estafeta, status, veiculo)
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
