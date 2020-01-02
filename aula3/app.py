from sqlalchemy import create_engine, Table, Column, MetaData, Integer, String, Text, select, ForeignKey, exc
from user import User

try:
    db = create_engine("postgresql+psycopg2://postgres:banco@192.168.99.100:5432/base01")
    print(db)
    metadados = MetaData()
    alunos = Table("alunos", metadados, Column("id", Integer, primary_key =True), Column("nome", String(60)))
    metadados.create_all(db)
    insert_command = alunos.insert().values(nome = "ze das quantas")
    print(insert_command)
    conn = db.connect()
    conn.execute(insert_command)

except Exception as e:
    print(e)