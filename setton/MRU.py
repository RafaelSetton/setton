class MRU:
    def __init__(self, velocidade=None, espaco=None, tempo=None):
        if velocidade is not None:
            self.velocidade = velocidade
        else:
            self.encontra_velocidade()
        if espaco is not None:
            self.espaco = espaco
        else:
            self.encontra_espaco()
        if tempo is not None:
            self.tempo = tempo
        else:
            self.encontra_tempo()

    def encontra_tempo(self):
        self.tempo = self.velocidade/self.espaco

    def encontra_velocidade(self):
        self.velocidade = self.espaco/self.tempo

    def encontra_espaco(self):
        self.espaco = self.velocidade*self.tempo
