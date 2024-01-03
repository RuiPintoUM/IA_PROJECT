class Encomenda:
    def __init__(self, id, localChegada, peso, volume, tempoPedido, distancia):
        self.id = id
        self.localChegada = localChegada
        self.peso = float(peso)
        self.volume = float(volume)
        self.tempoPedido = float(tempoPedido)
        self.estado = 0
        self.distancia = float(distancia)
