from sqlalchemy import create_engine


class DbUtils:
    db_string = "postgresql+psycopg2://postgres:banco@192.168.99.100:5432/streamFilmes"
    bd_query = " "

    def createTable(self):
        db = create_engine(self.db_string)
        self.db_query = "CREATE TABLE filmes (id_filme SERIAL PRIMARY KEY, nome VARCHAR(60), categoria VARCHAR(40), dataLancamento VARCHAR(40));"
        try:
            db.execute(self.db_query)
            res = True
        except:
            print("Problema ao criar a tabela \n")
            res = False
        return res

    def addNovoFilme(self, nome, categoria, dataLancamento):
        db = create_engine(self.db_string)
        try:
            db.execute("INSERT INTO filmes(nome, categoria, dataLancamento) VALUES(%s,%s,%s)",
                       nome, categoria, dataLancamento)
            res = True
        except:
            print("Problemas ao inserir na tabela filmes \n")
            res = False
        return res

    def updateFilme(self, id, nome, categoria, dataLancamento):
        db = create_engine(self.db_string)
        try:
            db.execute("UPDATE filmes SET nome=%s,categoria=%s,dataLancamento=%s WHERE id_filme=%s",
                       nome, categoria, dataLancamento, id)
            res = True
        except:
            print("Problemas ao atualizar na tabela filmes \n")
            res = False
        return res

    def verFilmes(self):
        db = create_engine(self.db_string)
        try:
            select = db.execute(
                "SELECT id_filme, nome, categoria, dataLancamento FROM filmes;")
            res = select
        # except Exception as e:
        except:
            res = False
        return res

    def verFilme(self, id):
        db = create_engine(self.db_string)
        try:
            select = db.execute(
                "SELECT * FROM public.filmes WHERE id_filme = %s;", id)
            res = select
        # except Exception as e:
        except:
            res = False
        return res
