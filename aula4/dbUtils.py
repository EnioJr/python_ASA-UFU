from sqlalchemy import create_engine


class DbUtils:
    db_string = "postgresql+psycopg2://postgres:banco@192.168.99.100:5432/base01"
    bd_query = " "

    def createTable(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE usuarios (id_usuario SERIAL PRIMARY KEY, nome VARCHAR(60), idade INT, cidade VARCHAR(40));"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problema ao criar a tabela \n")
            res = False
        return res

    def addNovoUsuario(self, nome, idade, cidade):
        db = create_engine(self.db_string)
        try:
            db.execute(
                "INSERT INTO usuarios(nome, idade, cidade) VALUES(%s,%s,%s)", nome, idade, cidade)
            res = True
        except:
            print("Problemas ao inserir na tabela usuário \n")
            res = False
        return res

    def updateUsuario(self, id, nome, idade, cidade):
        db = create_engine(self.db_string)
        try:
            db.execute(
                "UPDATE usuarios SET nome=%s,idade=%s,cidade=%s WHERE id_usuario=%s", nome, idade, cidade, id)
            res = True
        except:
            print("Problemas ao atualizar na tabela usuários \n")
            res = False
        return res

    def verUsuarios(self):
        db = create_engine(self.db_string)
        try:
            select = db.execute(
                "SELECT id_usuario, nome, idade, cidade FROM usuarios;")
            res = select
        # except Exception as e:
        except:
            res = False
        return res

    def verUsuario(self, id):
        db = create_engine(self.db_string)
        try:
            select = db.execute(
                "SELECT * FROM public.usuarios WHERE id_usuario = %s;", id)
            res = select
        # except Exception as e:
        except:
            res = False
        return res
