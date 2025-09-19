# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class LoginForm(FlaskForm):
    email = StringField('Usuário ou E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Informe a sua senha', validators=[DataRequired()])
    disciplina = SelectField('Informe a sua disciplina',
                             choices=[('DSWA5', 'DSWA5'),
                                      ('DWBA4', 'DWBA4'),
                                      ('Gestão de Projetos', 'Gestão de Projetos')],
                             validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    ip_address = request.remote_addr
    host = request.host

    if form.validate_on_submit():
        session['email'] = form.email.data
        session['disciplina'] = form.disciplina.data
        session['institution'] = "Instituto Federal de Educação, Ciência e Tecnologia de São Paulo - IFSP"
        flash(f'Bem-vindo, {session["email"]}!')
        return redirect(url_for('index'))

    return render_template(
        'index.html',
        form=form,
        email=session.get('email'),
        disciplina=session.get('disciplina'),
        institution=session.get('institution'),
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

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/user/<nome>')
def user(nome):
    return render_template('user.html', nome=nome)

@app.route('/rotainexistente')
def erro():
    return render_template('404.html')
