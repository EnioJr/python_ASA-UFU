from flask import render_template, flash, redirect, session
from app import app, db
from app.models.tables import User
from app.models.forms import LoginForm
from flask_login import login_user
#import wiringpi


"""wiringpi.wiringPiSetup()
wiringpi.wiringPiSetupSys()
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(16, 1)"""


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])


def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        session['usuario_logado'] = form.username.data
        if user and str(user.password) == str(form.data['password']):
            login_user(user)
            return render_template("index.html")
        else:
            pass
    return render_template("login.html", form = form)

@app.route("/cadastro")

def cadastro():
    return render_template("cadastro.html")


@app.route("/sala/<confsala>")
@app.route("/sala", defaults={"confsala" : None})

def sala(confsala):
    if confsala == "ligar":
        print(confsala)
        #wiringpi.digitalWrite(16, 1)
    elif confsala == "desligar":
        print(confsala)
        #wiringpi.digitalWrite(16, 0)
    return render_template("sala.html")

@app.route("/cozinha/<confcozinha>")
@app.route("/cozinha", defaults={"confcozinha" : None})

def cozinha(confcozinha):

    if confcozinha == "ligar":
        print(confcozinha)
        #wiringpi.digitalWrite(16, 1)
    elif confcozinha == "desligar":
        print(confcozinha)
        #wiringpi.digitalWrite(16, 0)
    return render_template("cozinha.html")

@app.route("/banheiro/<confbanheiro>")
@app.route("/banheiro", defaults={"confbanheiro" : None})

def banheiro(confbanheiro):
    if confbanheiro == "ligar":
        print(confbanheiro)
        #wiringpi.digitalWrite(16, 1)
    elif confbanheiro == "desligar":
        print(confbanheiro)
        #wiringpi.digitalWrite(16, 0)
    return render_template("banheiro.html")

@app.route("/copa/<confcopa>")
@app.route("/copa", defaults={"confcopa" : None})

def copa(confcopa):
    if confcopa == "ligar":
        print(confcopa)
        #wiringpi.digitalWrite(16, 1)
    elif confcopa == "desligar":
        print(confcopa)
        #wiringpi.digitalWrite(16, 0)
    return render_template("copa.html")

@app.route("/escritorio/<confescritorio>")
@app.route("/escritorio", defaults={"confescritorio" : None})

def escritorio(confescritorio):
    if confescritorio == "ligar":
        print(confescritorio)
        #wiringpi.digitalWrite(16, 1)
    elif confescritorio == "desligar":
        print(confescritorio)
        #wiringpi.digitalWrite(16, 0)
    return render_template("escritorio.html")

@app.route("/quarto1/<confquarto1>")
@app.route("/quarto1", defaults={"confquarto1" : None})

def quarto1(confquarto1):
    if confquarto1 == "ligar":
        print(confquarto1)
        #wiringpi.digitalWrite(16, 1)
    elif confquarto1 == "desligar":
        print(confquarto1)
        #wiringpi.digitalWrite(16, 0)
    return render_template("quarto1.html")

@app.route("/quarto2/<confquarto2>")
@app.route("/quarto2", defaults={"confquarto2" : None})

def quarto2(confquarto2):
    if confquarto2 == "ligar":
        print(confquarto2)
        #wiringpi.digitalWrite(16, 1)
    elif confquarto2 == "desligar":
        print(confquarto2)
        #wiringpi.digitalWrite(16, 0)
    return render_template("quarto2.html")

@app.route("/quarto3/<confquarto3>")
@app.route("/quarto3", defaults={"confquarto3" : None})

def quarto3(confquarto3):
    if confquarto3 == "ligar":
        print(confquarto3)
        #wiringpi.digitalWrite(16, 1)
    elif confquarto3 == "desligar":
        print(confquarto3)
        #wiringpi.digitalWrite(16, 0)
    return render_template("quarto3.html")

@app.route("/tabela")
def tabela():
    return render_template("tabela.html")