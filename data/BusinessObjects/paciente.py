class paciente:
    def __init__(self, id, numeroCartaoSus, cpf, alergias, historicoFamiliar, doencasPreexistentes, usuario ):
        self.id = id
        self.numeroCartaoSus = numeroCartaoSus
        self.alergias = alergias
        self.historicoFamiliar = historicoFamiliar
        self.doencasPreexistentes = doencasPreexistentes
        self.usuario = usuario
        self.cpf = cpf

    def setId(self, id):
        self.id = id

    def setNumeroCartaoSus(self, numeroCartaoSus):
        self.numeroCartaoSus = numeroCartaoSus

    def setAlergias(self, alergias):
        self.alergias = alergias

    def setHistoricoFamiliar(self, historicoFamiliar):
        self.historicoFamiliar = historicoFamiliar

    def setDoencasPreexistentes(self, doencasPreexistentes):
        self.doencasPreexistentes = doencasPreexistentes

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setCpf(self, cpf):
        self.cpf = cpf;

    def getId(self):
        return self.id

    def getNumeroCartaoSus(self):
        return self.numeroCartaoSus

    def getAlergias(self):
        return self.alergias

    def getHistoricoFamiliar(self):
        return self.historicoFamiliar

    def getDoencasPreexistentes(self):
        return self.doencasPreexistentes

    def getUsuario(self):
        return self.usuario
