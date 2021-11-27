class usuario:
    def __init__(self, id, nome, dataNascimento, login, senha):
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.login = login
        self.senha = senha

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setDataNascimento(self, dataNascimento):
        self.dataNascimento = dataNascimento

    def setLogin(self, login):
        self.login = login

    def setSenha(self, senha):
        self.senha = senha

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getDataNascimento(self):
        return self.dataNascimento

    def getLogin(self):
        return self.login

    def setSenha(self):
        return self.senha