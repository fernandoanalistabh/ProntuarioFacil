import conexao
con=conexao('localhost','regiao','postgres','12345')
sql = "create table usuario (id serial primary key, nome varchar(100), dataNascimento date, login varchar(10), senha varchar(10))"
if con.manipular(sql):
  print('inserido com sucesso!')
print(con.proximaPK('usuario', 'id'))
rs=con.consultar("select * from usuario")
for linha in rs:
  print (linha)
con.fechar()