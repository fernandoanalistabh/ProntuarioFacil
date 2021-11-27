import psycopg2
class conexao():
   _db=None
   def __init__(self):
       self._db = psycopg2.connect(host='localhost', database='prontuariofacil', user='postgres', password='12345')

   def manipular(self, sql):
       try:
           cur = self._db.cursor()
           cur.execute(sql)
           cur.close();
           self._db.commit()
       except:
           return False;
       return True

   def consultar(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            print(sql)
            cur.execute(sql)
            rs=cur.fetchall();
        except:
            return None
        return rs
   def proximaPK(self, tabela):
       sql='select max(id) from '+tabela
       rs = self.consultar(sql)
       pk = rs[0][0]
       return pk+1

   def fechar(self):
       self._db.close