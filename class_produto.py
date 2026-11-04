from abc import ABC, abstractmethod
class Produto(ABC):
    def __init__(self, nome, preco,estoque,descricao):
        self._nome = nome
        self._preco = preco
        self._estoque = estoque
        self._descricao = descricao
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self):
        self._nome = nome
    @property
    def preco(self):
        return self._preco
    @preco.setter
    def preco(self, preco):
        self._preco = preco
    @property
    def estoque(self):
        return self._estoque
    @estoque.setter
    def estoque(self, estoque):
        self._estoque = estoque
    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao
    @abstractmethod
    def criar_produto(self):
        pass
    @abstractmethod
    def atualizar_produto(self):
        pass
    @abstractmethod
    def deletar_produto(self):
        pass
    @abstractmethod
    def editar_produto(self):
        pass
    @abstractmethod
    def visualizar_produto(self):
        print("Nome:", self.nome)
        print("Preço: R$", self.preco)
        print("Descrição:", self.descricao)
        print("Estoque:", self.estoque, "unidades")