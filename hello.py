# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class LoginForm(FlaskForm):
    email = StringField('Usuário ou E-mail', validators=[DataRequired()])
    password = PasswordField('Informe a sua senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class HomeForm(FlaskForm):
    nome = StringField('Informe o seu nome', validators=[DataRequired()])
    sobrenome = StringField('Informe o seu sobrenome', validators=[DataRequired()])
    instituicao = StringField('Informe a sua Instituição de ensino', validators=[DataRequired()])
    disciplina = SelectField('Informe a sua disciplina',
                             choices=[('DSWA5', 'DSWA5'),
                                      ('DWBA4', 'DWBA4'),
                                      ('Gestão de Projetos', 'Gestão de Projetos')],
                             validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = HomeForm()
    ip_address = request.remote_addr
    host = request.host

    if form.validate_on_submit():
        session['nome'] = form.nome.data
        session['sobrenome'] = form.sobrenome.data
        session['instituicao'] = form.instituicao.data
        session['disciplina'] = form.disciplina.data
        return redirect(url_for('index'))

    return render_template(
        'index.html',
        form=form,
        nome=session.get('nome'),
        sobrenome=session.get('sobrenome'),
        instituicao=session.get('instituicao'),
        disciplina=session.get('disciplina'),
        ip_address=ip_address,
        host=host
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        flash(f'Você entrou com sucesso como {session["email"]}!')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/user/<nome>')
def user(nome):
    return render_template('user.html', nome=nome)

@app.route('/rotainexistente')
def erro():
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True)
