import json
import os
from Grafo import Graph
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
        return enc

    def adicionarEstafeta(self, nome_estafeta, status, veiculo):
        estafeta = Estafeta(nome_estafeta, status, veiculo)
        self.mapEstafetas[nome_estafeta] = estafeta

    def loginEstafeta(self, nome):
        if nome in self.mapEstafetas:
            return True
        else:
            return False
        
    def estafetaMaisEcologico(self, peso, distancia, tempo):
        for estafeta in self.mapEstafetas.values():
            if estafeta.verficaViabilidade(peso, distancia, tempo):
                pass
            

    def guardarData(self):
        map_path = os.path.join('data', 'estafetas.json')
        existing_data = []

        for estafeta in self.mapEstafetas.values():
            new_estafeta_data = {
                "nome": estafeta.nome,
                "status": estafeta.status,
                "veiculo": estafeta.veiculo,
                "numEntregas": estafeta.numEntregas,
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
                    numEntregas=estafeta_data["numEntregas"],
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

        encomenda.estafeta.status = 0

    def espacoLivreEstafeta(self, nome):
        estafeta = self.mapEstafetas.get(nome)
        espacoOcupado = estafeta.somaEncomendas()

        match  estafeta.veiculo:
            case "bicicleta":
                return 5 - espacoOcupado

            case "mota":
                return 20 - espacoOcupado

            case "carro":
                return 100 - espacoOcupado

    def printanomes(self):
        for estafeta in self.mapEstafetas.values():
            print(estafeta.nome)

    def executaTrabalho(self, local1, local2, local3):
        pass

    def mostrarEncomendasDisponiveis(self, nome):
        estafeta = self.mapEstafetas.get(nome)

        listaEncomendas = []

        for encomenda in self.listaEncomendas:
            if encomenda.estado == 0 and estafeta.verificaAddEncomenda(encomenda) :
                listaEncomendas.append(encomenda)

        return listaEncomendas

    def atribuiEncomenda(self, nome, encomenda):
        estafeta = self.mapEstafetas.get(nome)

        encomenda.estado = 1
        estafeta.listaEncomenda.append(encomenda)

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
        print(result_BFS)
        result_DFS = self.grafo.procura_DFS("Central", local)
        print(result_DFS)
        result_Greedy = self.grafo.greedy("Central", local)
        print(result_Greedy)
        result_Astar = self.grafo.procura_aStar("Central", local)
        print(result_Astar)

        results = [result_BFS, result_DFS, result_Greedy, result_Astar]
        valid_results = [result for result in results if result is not None]

        if not valid_results:
            return None

        min_result = min(valid_results, key=lambda x: x[1])
        melhorCaminho, custoMin = min_result

        print("Melhor Caminho:", melhorCaminho)
        print("Custo Mínimo:", custoMin)

        return min_result
        
    def mostrarListaEncomendas(self, nome):
        estafeta = self.mapEstafetas.get(nome)
        
        return estafeta.getEncomendas()

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
