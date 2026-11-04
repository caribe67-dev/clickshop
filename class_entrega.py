class Entrega:
    def __init__(self, endereco,rastreio, status):
        self._endereco = endereco
        self._rastreio = rastreio
        self._status = status
    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    @property
    def rastreio(self):
        return self._rastreio
    @rastreio.setter
    def rastreio(self, rastreio):
        self._rastreio = rastreio
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status