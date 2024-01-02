class Encomenda:

    def __init__(self, localChegada, peso, volume, tempoPedido, distancia):
        self.localChegada = localChegada
        self.peso = float(peso)
        self.volume = float(volume)
        self.tempoPedido = float(tempoPedido)
        self.estado = 0 # 0 -> por atribuir 1 -> atribuida
        self.distancia = float(distancia)

    def defineVeiculo(self):
        if ((self.tempoB < self.tempoPedido) and (self.peso < 5)) or (self.tempoPedido == 0):
            self.veiculo = "Bicicleta"
            self.tempoReal = self.tempoB
        elif (self.tempoM < self.tempoPedido) and (self.peso < 20):
            self.veiculo = "Mota"
            self.tempoReal = self.tempoM
        elif (self.tempoC < self.tempoPedido) and (self.peso < 100):
            self.veiculo = "Carro"
            self.tempoReal = self.tempoC
        else:
            self.veiculo = "na"
            self.tempoReal = "na"

    def definePreco(self):
        if(self.veiculo == "Bicicleta"): self.preco = 0.05 * self.distancia
        elif (self.veiculo == "Mota"): self.preco = 0.10 * self.distancia
        elif (self.veiculo == "Carro"): self.preco = 0.50 * self.distancia
        else: self.preco = 0
