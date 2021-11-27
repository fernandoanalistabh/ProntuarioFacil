import psycopg2
con = psycopg2.connect(host='localhost', database='prontuariofacil', user='postgres', password='12345')
cur = con.cursor()

sql = 'DROP TABLE IF EXISTS medicacao;'
cur.execute(sql)
con.commit()

sql = 'DROP TABLE IF EXISTS evento;'
cur.execute(sql)
con.commit()

sql = 'DROP TABLE IF EXISTS paciente;'
cur.execute(sql)
con.commit()

sql = 'DROP TABLE IF EXISTS medico;'
cur.execute(sql)
con.commit()

sql = 'DROP TABLE IF EXISTS usuario;'
cur.execute(sql)
con.commit()

sql = 'create table usuario (id int primary key, nome varchar(100), dataNascimento date, login varchar(10), senha varchar(10))'
cur.execute(sql)
con.commit()

sql = 'create table paciente (id int primary key, numeroCartaoSus varchar(10), cpf varchar (11), alergias varchar(300), historicoFamiliar varchar(300), doencasPreexistentes varchar(300), id_usuario int, CONSTRAINT fk_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id))'
cur.execute(sql)
con.commit()

sql = 'create table medico (id int primary key, crm varchar(10), id_usuario int, CONSTRAINT fk_usuario FOREIGN KEY(id_usuario) REFERENCES usuario(id))'
cur.execute(sql)
con.commit()

sql = 'create table evento (id int primary key, observacoes varchar (300), dataInicio date, dataFim date, id_medico int, CONSTRAINT fk_medico FOREIGN KEY(id_medico) REFERENCES medico(id), id_paciente int, CONSTRAINT fk_paciente FOREIGN KEY(id_paciente) REFERENCES paciente(id))'
cur.execute(sql)
con.commit()

sql = 'create table medicacao (id int primary key, nome varchar (100), dataPrescrito date, tipo varchar(10), dataInicio date, dataFim date, id_evento int, CONSTRAINT fk_evento FOREIGN KEY(id_evento) REFERENCES evento(id))'
cur.execute(sql)
con.commit()

sql = "insert into usuario values (1,'Fernando Jose', '12/12/2000', '12345678', '123456789')"
cur.execute(sql)
con.commit()

sql = "insert into paciente values (1, '123456789', '12345678988', 'alergias', 'historico', 'doencasPreexistentes', 1)"
cur.execute(sql)
con.commit()

sql = "insert into usuario values (2,'joao', '12/12/2000', '12345', '12345')"
cur.execute(sql)
con.commit()

sql = "insert into medico values (1, '123', 2)"
cur.execute(sql)
con.commit()

sql = "insert into evento values (1, 'O paciente está evoluindo muito bem.', '01/12/2021', '01/12/2021', 1, 1)"
cur.execute(sql)
con.commit()

sql = "insert into medicacao values (1, 'dipirona', '01/12/2021', 'regular', '01/12/2021', null, 1)"
cur.execute(sql)
con.commit()

sql = "insert into medicacao values (2, 'dorflex', '01/12/2021', 'temporário', '01/12/2021', null, 1)"
cur.execute(sql)
con.commit()

cur.execute('select * from usuario')
recset = cur.fetchall()

for rec in recset:
    print(rec)

cur.execute('select * from paciente')
recset = cur.fetchall()

for rec in recset:
    print(rec)

cur.execute('select * from medico')
recset = cur.fetchall()

for rec in recset:
    print(rec)

cur.execute('select * from medicacao')
recset = cur.fetchall()

for rec in recset:
    print(rec)

con.close()