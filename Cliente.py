class Cliente:

    def __init__(self, nome, estafetasPorAvaliar = []):
        self.nome = nome
        self.estafetasPorAvaliar = estafetasPorAvaliar

    def adicionaEstafetaParaAva(self, nome):
        self.estafetasPorAvaliar.append(nome)

    