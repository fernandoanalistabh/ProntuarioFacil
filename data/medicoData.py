from data import conexao
con = conexao.conexao()

def consultaMedico(id):
  return con.consultar("select * from medico where id = " + id + ";")