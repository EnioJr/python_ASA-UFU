from flask import Flask, render_template, request, json, jsonify
from flask_bootstrap import Bootstrap
from flask import flash

app = Flask(__name__)
app.config["SECRET_KEY"] = 'minha palavra secreta'
Bootstrap(app)

@app.route('/singUp')
def singUp():
    return render_template('signUp.html')

@app.route('/singUpUser', methods=['post'])
def singUpUser():
    user = request.form['username']
    password = request.form['password']
    print(user,password)
    return json.dumps({'status': 'ok', 'user': user, 'pass': password})

@app.route('/showMessage', methods=['Post'])
def showMessage():
    #return jsonify(dict(redirect='/sucess'))
    return json.dumps({'status': 'ok', 'message': 'Funcionou!'})

@app.route('/sucess', methods=['GET'])
def sucess():
    return render_template('sucess.html')

@app.route('/')
def homepage():
    title ='ASA!'
    paragraph= 'teste'
    message = 'Funcionou'

    try:
        return render_template('index.html', title = title, paragraph =paragraph, message = message)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = '8080' )