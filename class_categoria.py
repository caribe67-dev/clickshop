class Categoria:
    def __init__(self, nome, descrição):
        self._nome = nome
        self._descrição = descrição
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @property
    def descrição(self):
        return self._descrição
    @descrição.setter
    def descrição(self, descrição):
        self._descrição = descrição