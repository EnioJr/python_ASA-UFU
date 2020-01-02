from flask import Flask, url_for, request, json, jsonify
from user import User
from json import dumps

app = Flask(__name__) #Sempre chama assim

myUser = [] #Cria o vetor que vair receber os alunos

@app.route('/') #Representa a parte final da url, nesse caso, não tem nada alem do ip
def api_root():
    return 'Seja bem vindo!!!'

@app.route('/hello')
def api_hello():
    if 'nome' in request.args:
        return 'Olá ' + request.args['nome']
    else:
        return 'Olá desconhecido!!'

@app.route('/hello2')
def api_hello2():
    if 'nome' in request.args:
        return 'Olá ' + request.args['nome'] + ' ' + request.args['sobrenome']
    else:
        return 'Olá desconhecido!!'

@app.route('/api/createusers')
def api_createusers():
    global myUser
    myUser.append(User(1, "Joao", 12, "São Paulo"))
    myUser.append(User(2, "Pedro", 13, "São Tomé"))
    myUser.append(User(3, "Jorge", 14, "São Bernado"))
    myUser.append(User(4, "Valdir", 11, "São Roque"))
    myUser.append(User(5, "Antonio", 10, "São Cristóvão"))
    res = {'status': 'Ok'}
    return jsonify(res)

@app.route('/api/listusers', methods = ['GET'])
def api_listusers():
    global myUser
    payload = []
    content = {}

    for elem in myUser:
        content = {'id': str(elem.getUserId()), '[nome]': elem.getUserNome(), '[idade]': str(elem.getUserIdade()), '[cidade]': elem.getUserCidade()}
        payload.append(content)
        content = {}

    res = json.dumps(payload)

    return jsonify(UserList=res)

@app.route('/api/adduser', methods = ['POST']) 
def api_newUSER():
    global myUser
    req_data = request.get_json()

    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    cidade = req_data['cidade']
    new_user = User(id, nome, idade, cidade)
    myUser.append(new_user)
    res = {'status': 'ok'}
    return jsonify(res)
    #curl -d '{"id": "6", "nome": "Zezinho", "idade": "15", "cidade": "Uberlandia"}' -H "content-Type: application/json" -X POST http://localhost:5000/api/adduser

@app.route('/api/getuser', methods = ['GET'])
def api_getuser():
    global myUser
    user_data = request.get_json()
    print(user_data)
    codUser = user_data['codigo']
    print(codUser)
    print(myUser[0].getUserNome())
    res = {'status': 'Usuario nao encontrado!'}
    for elem in myUser:
        if(int(codUser) == elem.getUserId()):
            res = {'nome': elem.getUserNome()}

    return jsonify(res)

#@app.route('/echo', methods = ['GET', 'POST', 'PUT', 'DELETE'])
#def api_echo():
#    if request.method == 'GET':
#        return "ECHO: GET\n"
#    elif request.method == 'POST':
#        return "ECHO: POST\n"
#    elif request.method == 'PUT':
#        return "ECHO: PUT\n"
#    elif request.method == 'DELETE':
#        return "ECHO: DELETE\n"


if __name__ == 'main':
    app.run()