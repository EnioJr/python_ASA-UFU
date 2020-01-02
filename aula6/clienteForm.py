from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required

class ClienteForm(FlaskForm):
    nome = StringField('Entre com o seu nome', validators=[Required()])
    submit = SubmitField('Enviar')