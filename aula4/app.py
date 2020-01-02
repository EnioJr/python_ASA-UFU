from flask import Flask, url_for, request, json, jsonify, abort
from json import dumps
from dbUtils import DbUtils

app = Flask(__name__) #Sempre chama assim
myUser = [] #Cria o vetor que vair receber os alunos

@app.route('/')
def api_root():
    return "Seja Bem Vindo!!!"

@app.route('/createdbuser')
def api_createuserdb():
    dbUtils = DbUtils()
    if (dbUtils.createTable()):
        result = {"result": "Tabela de usuários criada!"}
    else:
        result = {"result": "Problemas para criar Tabela de usuários!"}
    return jsonify(result)

@app.route('/adduserdb', methods = ['POST'])
def api_newuserdb():
            
    dbUtils = DbUtils()
    req_data = request.get_json()
    if not request.json:
        abort(400)

    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    if (dbUtils.addNovoUsuario(nome, idade, cidade)):
        result = {"result": "usuário criado!"}
    else:
        result = {"result": "Problemas para criar usuário!"}
    return jsonify(result)

@app.route('/updateuserdb', methods = ['POST'])
def api_updateuserdb():
    dbUtils = DbUtils()
    req_data = request.get_json()
    if not request.json:
        abort(400)

    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    if (dbUtils.updateUsuario(id, nome, idade, cidade)):
        result = {"result": "usuário editado!"}
    else:
        result = {"result": "Problemas para editar usuário!"}
    return jsonify(result)

@app.route('/listuserdb', methods = ['POST'])
def api_listuserdb():
    users =[]
    dbUtils = DbUtils()
    result = dbUtils.verUsuarios()    
    if (result):
        for row in result:
            users.append({
                "id": row['id_usuario'],
                "nome": row['nome'],
                "idade": row['idade'],
                "cidade": row['cidade']})
        result = {"result": users}
    else:
        result = {"result": "Problemas para editar usuário!"}
    return jsonify(result)


@app.route('/veruserdb', methods = ['POST'])
def api_veruserdb():
    dbUtils = DbUtils()
    req_data = request.get_json()
    if not request.json:
        abort(400)
    id = req_data['id']
    dbUtils = DbUtils()
    result = dbUtils.verUsuario(id)    
    if (result):        
        for row in result:
            user = {
            "id": row['id_usuario'],
            "nome": row['nome'],
            "idade": row['idade'],
            "cidade": row['cidade']}
        result =  user
    else:
        result = {"result": "Problemas para editar usuário!"}
    return jsonify(result)

if __name__ == 'main':
    app.run()