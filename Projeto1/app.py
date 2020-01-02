from flask import Flask, render_template, flash, url_for, request, json, jsonify, abort, redirect
from flask_bootstrap import Bootstrap
from filmeForm import FilmeForm
from dbUtils import DbUtils
from json import dumps

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha palavra chave"
Bootstrap(app)


@app.route("/")
def homepage():
    title = "Arquitetura de Software Aplicada!!"
    paragraph = "Esta a primeira página com reinderização!!"
    message = "Funcionou!!"

    try:
        return render_template('index.html', title=title, paragraph=paragraph, message=message)
    except Exception as e:
        return str(e)


@app.route("/addFilme", methods=['GET', 'POST'])
def index():
    dbUtils = DbUtils()

    nome = None
    form = FilmeForm()
    if form.validate_on_submit():
        if (dbUtils.createTable()):
            result = {"result": "Tabela de usuários criada!"}
        else:
            result = {"result": "Problemas para criar Tabela de usuários!"}

        nome = form.nome.data
        categoria = form.categoria.data
        dataLancamento = form.dataLancamento.data

        dbUtils.addNovoFilme(nome, categoria, dataLancamento)
        result = {"result": "usuário criado!"}

    return render_template('cadastro.html', form=form, nome=nome)

# --------------------------------------------Testando metodos aqui---------------------------------------------


@app.route('/updateFilme', methods=['POST'])
def updatefilmedb():
    dbUtils = DbUtils()

    nome = None
    form = FilmeForm()

    if form.validate_on_submit():
        id = form.id.data
        nome = form.nome.data
        categoria = form.categoria.data
        dataLancamento = form.dataLancamento.data

        if (dbUtils.updateFilme(id, nome, categoria, dataLancamento)):
            result = {"result": "usuário editado!"}
        else:
            result = {"result": "Problemas para editar usuário!"}
        return jsonify(result)

# Funcionando metodo
@app.route('/verFilmes', methods=['GET'])
def verfilmesdb():
    users = []
    dbUtils = DbUtils()
    result = dbUtils.verFilmes()
    if (result):
        for row in result:
            users.append({
                "id": row['id_filme'],
                "nome": row['nome'],
                "categoria": row['categoria'],
                "dataLancamento": row['datalancamento']})
        result = {"result": users}
    else:
        result = {"result": "Problemas para editar usuário!"}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
