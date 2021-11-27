class medico:
    def __init__(self, id, crm, usuario):
        self.id = id
        self.crm = crm
        self.usuario = usuario

    def setId(self, id):
        self.id = id

    def setCrm(self, crm):
        self.crm = crm

    def setUsuario(self, usuario):
        self.usuario = usuario

    def getId(self):
        return self.id

    def getCrm(self):
        return self.crm

    def getUsuario(self):
        return self.usuario

