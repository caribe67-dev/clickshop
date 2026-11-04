class Endereco:
    def __init__(self, rua, numero, cidade, CEP):
        self._rua = rua
        self._numero = numero
        self._cidade = cidade
        self._CEP = CEP

    @property
    def rua(self):
        return self._rua

    @rua.setter
    def rua(self, rua):
        self._rua = rua

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def CEP(self):
        return self._CEP
    
    @CEP.setter
    def CEP(self, CEP):
        self._CEP = CEP
    