from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def homepage():
    title = "Arquitetura de Software Aplicada!!"
    paragraph = "Teste"
    message = "Funcionou!!"

    try:
        return render_template("index.html", title = title, paragraph = paragraph, message = message)
    except Exception as e:
        return str(e)

@app.route("/disciplina")
def show_disciplina():
    username = "João"
    lista_disc = {'IEC', 'CALC2', 'ASA', 'BD'}
    dict_disc = {'IEC':45, 'CALC2':45, 'ASA':60, 'BD':60}
    return render_template('disciplinas.html', username=username,lista_disc=lista_disc, dict_disc=dict_disc)

@app.route("/seila")
def show_seila():
    try:
        return render_template("index2.html")
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 8080)