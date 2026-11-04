from abc import ABC, abstractmethod
class UsuarioBase(ABC):
    def __init__(self, nome, email, senha,endereco,cpf):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._endereco = endereco
        self._cpf = cpf
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    @abstractmethod
    def cadastrar(self):
        pass
    @abstractmethod
    def autenticar(self):
        pass
    @abstractmethod
    def editar(self):
        pass
    @abstractmethod
    def deletar(self):
        pass