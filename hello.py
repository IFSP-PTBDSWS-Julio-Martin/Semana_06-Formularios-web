# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'  # Necessário para forms e flash

bootstrap = Bootstrap(app)
moment = Moment(app)

class LoginForm(FlaskForm):
    email = StringField('Usuário ou E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Informe a sua senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = LoginForm()
    if form.validate_on_submit():
        # Simulando login com um e-mail específico
        session['email'] = form.email.data
        flash(f'Bem-vindo, {session["email"]}!')
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form, email=session.get('email'))

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
