class medicacao:
    def __init__(self, id, nome, dataPrescrito, tipo, dataInicio, dataFim, evento):
        self.id = id
        self.nome = nome
        self.dataPrescrito = dataPrescrito
        self.tipo = tipo
        self.dataIncio = dataInicio
        self.dataFim = dataFim
        self.evento = evento

    def setId(self, id):
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setDataPrescrito(self, dataPrescrito):
        self.dataPrescrito = dataPrescrito

    def setTipo(self, tipo):
        self.tipo = tipo

    def setInicio(self, dataInicio):
        self.dataIncio = dataInicio

    def setDataFim(self, dataFim):
        self.dataFim = dataFim

    def setEvento(self, evento):
        self.evento

    def getId(self):
        return self.id

    def getNome(self):
        return self.Nome

    def getDataPrescrito(self):
        return self.dataPrescrito

    def getTipo(self, tipo):
        return self.tipo

    def getInicio(self):
        return self.dataIncio

    def getDataFim(self):
        return self.dataFim

    def getEvento(self):
        self.evento
