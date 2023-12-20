class Estafeta:
    def __init__(self, nome, status):
        self.nome = nome
        self.status = status
        self.encomenda_ids = []  # Use a list to store encomenda IDs

    def addEncomenda(self, id_encomenda):
        self.encomenda_ids.append(id_encomenda)

