from data import conexao
con = conexao.conexao()

def consultaPaciente(nome, cpf):
  return con.consultar("select * from paciente p inner join usuario u on (u.id = p.id_usuario) where u.nome like '%" + nome + "%' or p.cpf like '%" + cpf + "%';")