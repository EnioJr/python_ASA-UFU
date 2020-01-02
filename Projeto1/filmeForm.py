from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Required


class FilmeForm(FlaskForm):
    nome = StringField('Entre com o seu nome', validators=[Required()])
    categoria = StringField('Entre com a sua categoria',
                            validators=[Required()])
    dataLancamento = StringField(
        'Entre com a data de lancamento', validators=[Required()])
    submit = SubmitField('Enviar')
