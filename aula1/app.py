from flask import Flask,url_for,request,json,jsonify
from user import User

myUser = [] #Cria o vetor que vair receber os alunos

app = Flask(__name__)
@app.route('/')
def api_root():
    return "Seja bem vindo!"

@app.route('/hello')
def api_hello():
    if 'nome' in request.args:
        return 'Olá' + request.args['nome']
    else:
        return 'Olá desconhecido!!'

@app.route('/echo', methods = ['GET', 'POST','PUT','DELETE','PATCH'])
def api_echo():
    if request.method == 'GET':
        return 'METODO: GET\n'
    elif request.method == 'POST':
        return 'METODO: POST\n'
    elif request.method == 'PUT':
        return 'METODO: PUT\n'
    elif request.method == 'DELETE':
        return 'METODO: DELETE\n'
    else:
        return 'metodo não reconhecido!!'

@app.route('/api/createusers')
def api_createusers():
    global myUser
    myUser.append(User(1,"Joao", 12, "São Paulo"))
    myUser.append(User(2,"Joao", 14, "São Paulo"))
    myUser.append(User(3,"Joao", 13, "São Paulo"))
    myUser.append(User(4,"Joao", 11, "São Paulo"))
    myUser.append(User(5,"Joao", 10, "São Paulo"))
    res = {'status': 'Ok'}
    return jsonify(res)

#fazer um endpoint para cadastrar aluno, criar vetor global, passando parametros
#com nome= &
if __name__ == 'main':
    app.run()