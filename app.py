#coding: utf-8

from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class Pessoa(db.Model):
        __tablename__ = 'cliente'
        _id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        nome = db.Column(db.String)
        telefone = db.Column(db.String)
        cpf = db.Column(db.String)
        email = db.Column(db.String)

        def __init__(self, nome, telefone, cpf, email):
            self.nome = nome
            self.telefone = telefone
            self.cpf = cpf
            self.email = email
#Cria no banco de dados
db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrar"):
def cadastrar():
    return render_template("cadastro.html")

@app.route("/cadastro", method = ['GET', 'POST']):
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome") 


if __name__  == '__main__':
    app.run(debug= True)

