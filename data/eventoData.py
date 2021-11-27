from data import conexao
from data import medicacaoData
con = conexao.conexao()

def consultaEventoPorPaciente(idPaciente):
  return con.consultar("select * from evento where id_paciente = " + idPaciente + ";")

def consultaEventoPorId(id):
  return con.consultar("select * from evento where id = " + id + ";")

def insereEvento(evento):
  for medicacao in evento.medicacoes:
    medicacaoData.insereMedicacao(medicacao)
  return con.manipular("insert into evento(id, observacoes, dataInicio, dataFim, id_medico, id_paciente) values (" + con.proximaPK("evento") + ", " + evento.observacoes + ", " + evento.dataInicio + ", " + evento.dataFim + ", " + evento.medico.id + ", " + evento.paciente.id + ");")

def editaEvento(evento):
  for medicacao in evento.medicacoes:
    medicacaoData.editaMedicacao(medicacao)
  return con.manipular("update evento set observacoes = " + evento.observacoes + ", dataInicio = " + evento.dataInicio + ", dataFim = " + evento.dataFim + ", idMedico = " + evento.medico.id + ", idPaciente = " + evento.paciente.id + " where id = " + evento.id + ";")

def deletaEvento(id):
  return con.manipular("delete from evento where id = " + id + ";")