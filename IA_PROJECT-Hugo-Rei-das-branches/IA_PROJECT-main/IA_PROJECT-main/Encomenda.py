class Encomenda:

    def __init__(self, id, localChegada, peso, volume, tempoPedido, distancia):
        self.id = id
        self.localChegada = localChegada
        self.peso = float(peso)
        self.volume = float(volume)
        self.tempoPedido = float(tempoPedido)
        #self.estafeta
        self.distancia = float(distancia)
        self.tempoB = self.tempoBicla()
        self.tempoM = self.tempoMota()
        self.tempoC = self.tempoCarro()
        self.defineVeiculo()
        self.definePreco()

    def tempoBicla(self):
        velocidade_bicla = 10  # Velocidade em km/h para bicicleta
        tempo_horas = self.distancia / velocidade_bicla
        return tempo_horas

    def tempoMota(self):
        velocidade_mota = 35  # Velocidade em km/h para mota
        tempo_horas = self.distancia / velocidade_mota
        return tempo_horas

    def tempoCarro(self):
        velocidade_carro = 50  # Velocidade em km/h para carro
        tempo_horas = self.distancia / velocidade_carro
        return tempo_horas


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


