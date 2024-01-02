class Estafeta:
    def __init__(self, nome, status, veiculo, numEntregas = 0, somaClassificacoes = 0):
        self.nome = nome
        self.status = status
        self.numEntregas = numEntregas
        self.veiculo = veiculo
        self.somaClassificacoes = somaClassificacoes
    
    def tempoBicla(self, distancia):
        return distancia / 10

    def tempoMota(self, distancia):
        return distancia / 35

    def tempoCarro(self, distancia):
        return distancia / 50
    
    def verficaViabilidade(self, peso, distancia, tempo):
        if self.veiculo == "bicicleta" and peso < 5 and self.tempoBicla(distancia) < tempo:
            return True
        elif self.veiculo == "mota" and peso < 20 and self.tempoMota(distancia) < tempo:
            return True
        elif self.veiculo == "carro" and peso < 100 and self.tempoCarro(distancia) < tempo:
            return True
        else:
            return False

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