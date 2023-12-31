class Estafeta:
    def __init__(self, nome, status, veiculo, somaClassificacoes = 0):
        self.nome = nome
        self.status = status
        self.listaEncomendaPorFazer = []
        self.veiculo = veiculo
        self.somaClassificacoes = somaClassificacoes

    def somaEncomendas(self):
        accumulator = 0

        for encomenda in self.listaEncomendaPorFazer():
            accumulator += encomenda.peso

        return accumulator

    def verificaAddEncomenda(self, encomenda):
        acumolador = self.somaEncomendas()

        acumolador += encomenda.peso

        match  self.veiculo:
            case 1:
                if acumolador < 5:
                    return True
                else:
                    return False
            case 2:
                if acumolador < 20:
                    return True
                else:
                    return False
            case 3:
                if acumolador < 100:
                    return True
                else:
                    return False

    def addEncomenda(self, encomenda):

        pesoEncomendas = self.somaEncomendas()
        self.encomenda_ids.append(encomenda)

    def getEncomendas(self):
        return self.encomenda_ids





