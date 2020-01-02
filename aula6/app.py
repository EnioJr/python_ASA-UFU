from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from clienteForm import ClienteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "minha palavra chave"
Bootstrap(app)

@app.route("/")
def homepage():
    title = "Arquitetura de Software Aplicada!!"
    paragraph = "Esta a primeira página com reinderização!! E qual foi o resultado de"
    message = "Funcionou!!"

    try:
        return render_template("index.html", title = title, paragraph = paragraph, message = message)
    except Exception as e:
        return str(e)

@app.route("/cliente", methods=['GET', 'POST'])
def index():
    nome = None
    form = ClienteForm()
    if form.validate_on_submit():
        nome = form.nome.data
    return render_template('index.html', form=form, nome=nome)

if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1", port = 8080)