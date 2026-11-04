class Pagamento:
    def __init__(self, metodo, valor,status):
        self._metodo = metodo
        self._valor = valor
        self._status = status

    @property
    def metodo(self):
        return self._metodo

    @metodo.setter
    def metodo(self, metodo):
        self._metodo = metodo

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor
        
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):   
        self._status = status