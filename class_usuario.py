from usuariobase import UsuarioBase


class Usuario(UsuarioBase):
    def __init__(self, nome, email, senha, endereco, cpf):
        super().__init__(nome, email, senha, endereco, cpf)

    def cadastrar(self):
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        endereco = input("Digite seu endereço: ")
        cpf = input("Digite seu CPF: ")

        cads = nome == self._nome and email == self._email and senha == self._senha and endereco == self._endereco and cpf == self._cpf
        if cads:
            print("Cadastro realizado com sucesso!")
        else:
            print("Cadastro não realizado.")

            
    def login(self):
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        if email == self._email and senha == self._senha:
            print("Login realizado com sucesso!")
        else:
            print("Email ou senha incorretos.")
    


