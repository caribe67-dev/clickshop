from produto import Produto 
class Compra(Produto):
    def __init__(self, nome, preco, estoque, descricao, quantidade):
        super().__init__(nome, preco, estoque, descricao)
        self._quantidade = quantidade

    def calcular_total(self):
        return self._preco * self._quantidade
    