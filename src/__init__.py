import os
from flask import Flask, jsonify, render_template, request, redirect, url_for, session  
from flask_sqlalchemy import SQLAlchemy
from src.models.employe import Employe
# from sqlalchemy import create_engine

def init_app() -> Flask:
    app = Flask(__name__)
    DB_STRING = os.environ.get(
    'DB_STRING', 'mysql://root:root@host.docker.internal/app')
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_STRING
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db = SQLAlchemy(app)

#   page d'accueil du site permettant de ce connecter
    @app.route("/")
    @app.route("/accueil", methods =['GET', 'POST'])
    def accueil():
        return render_template('accueil.html')

#   page d'inscription du site
    @app.route("/inscription", methods =['GET', 'POST'])
    def inscription():
        return render_template('inscription.html')

#   page de questionnaire du site avec toute les questions
    @app.route("/questionnaire")
    def questionnaire():
        return render_template('questionnaire.html')

#   page de questionnaire du site avec toute les questions
    @app.route("/index")
    def index():
        return render_template('index.html')

#   page de questionnaire du site avec toute les questions
    @app.route("/ouioui")
    def ouioui():
        employe = Employe.query.all()
        for e in employe:
            print(e.__repr__)
        return render_template("ouioui.html", msg=employe)    

    return app
