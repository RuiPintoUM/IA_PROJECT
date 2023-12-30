class Estafeta:
    def __init__(self, nome, status, somaClassificacoes = 0):
        self.nome = nome
        self.status = status
        self.encomenda_ids = []  # Use a list to store encomenda IDs
        self.somaClassificacoes = somaClassificacoes

    def addEncomenda(self, id_encomenda):
        self.encomenda_ids.append(id_encomenda)

    def getEncomendas(self):
        return self.encomenda_ids
