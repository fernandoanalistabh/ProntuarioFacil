from data import conexao
con = conexao.conexao()

def consultaMedicacao(id):
  return con.consultar("select * from medicacao where id = " + id + ";")

def insereMedicacao(medicacao):
  return con.manipular("insert into medicacao(id, nome, dataPrescrito, tipo, dataInicio, dataFim, id_evento) values (" + con.proximaPK("medicacao") + ", " + medicacao.nome + ", " + medicacao.dataPrescrito + ", " + medicacao.tipo + ", " + medicacao.dataIncio + ", " + medicacao.dataFim + ", " + medicacao.evento.id + ");")

def editaMedicacao(medicacao):
  return con.manipular("update medicacao set nome = " + medicacao.nome + ", dataPrescrito = " + medicacao.dataPrescrito + ", tipo = " + medicacao.tipo + ", dataInciio = " + medicacao.dataIncio + ", medicacao = " + medicacao.dataFim + ", id_evento = " + medicacao.evento.id + " where id = " + medicacao.id + ";")

def deletaMedicao(id):
  return con.manipular("delete from medicacao where id = " + id + ";");