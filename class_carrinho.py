from produto import Produto

class Carrinho(Produto):
    def __init__(self, nome, preco, estoque, descricao):
        self.produtos = []
        super().__init__(nome, preco, estoque, descricao)

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

    def listar_produtos(self):
        for produto in self.produtos:
            print("Produto:", produto.nome, ", Preço: R$", produto.preco, ", Descrição:", produto.descricao, ", Estoque:", produto.estoque, "unidades")