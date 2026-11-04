class Avaliacao:
    def __init__(self, nota, comentario):
        self.nota = nota
        self.comentario = comentario

    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self, nota):
        self._nota = nota  
    @property
    def comentario(self):
        return self._comentario
    @comentario.setter
    def comentario(self, comentario):
        self._comentario = comentario
    nota = input("Digite a nota da avaliação (1 a 5): ")
    comentario = input("Digite o comentário da avaliação: ")