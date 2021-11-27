class evento:
    def __init__(self, id, observacoes, dataInicio, dataFim, medico, paciente, medicacoes):
        self.id = id
        self.observacoes = observacoes
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.medico = medico
        self.paciente = paciente
        self.medicacoes = medicacoes

    def setId(self, id):
        self.id = id

    def setObservacoes(self, observacoes):
        self.observacoes = observacoes

    def setDataInicio(self, dataInicio):
        self.dataInicio = dataInicio

    def setDataFim(self, dataFim):
        self.dataFim = dataFim

    def setMedico(self, medico):
        self.medico = medico

    def setPaciente(self, paciente):
        self.paciente = paciente

    def setMedicacoes(self, medicacoes):
        self.medicacoes = medicacoes

    def getId(self, id):
        return self.id

    def getObservacoes(self):
        return self.observacoes

    def getDataInicio(self):
        return self.dataInicio

    def getDataFim(self):
        return self.dataFim

    def getMedico(self):
        return self.medico

    def getPaciente(self):
        return self.paciente

    def getMedicacoes(self):
        return self.medicacoes


