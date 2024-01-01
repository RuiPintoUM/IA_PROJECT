class Estafeta:
    def __init__(self, nome, status, veiculo, listaEncomenda = [], somaClassificacoes = 0):
        self.nome = nome
        self.status = status
        self.listaEncomenda = listaEncomenda
        self.veiculo = veiculo
        self.somaClassificacoes = somaClassificacoes

    def somaEncomendas(self):
        accumulator = 0

        for encomenda in self.listaEncomenda:
            accumulator += encomenda.peso

        return accumulator

    def verificaAddEncomenda(self, encomenda):
        acumolador = self.somaEncomendas()

        acumolador += encomenda.peso

        match  self.veiculo:
            case "bicicleta":
                if acumolador < 5:
                    return True
                else:
                    return False
            case "mota":
                if acumolador < 20:
                    return True
                else:
                    return False
            case "carro":
                if acumolador < 100:
                    return True
                else:
                    return False

    def getEncomendas(self):
        return self.encomenda_ids

