from data import conexao
con = conexao.conexao()

def consultaUsuario(id):
  return con.consultar("select * from usuario where id =" + id + ";")

def consultaLogin(login, senha):
    return con.consultar("select * from usuario where login = " + login + " and senha = " + senha + ";")
