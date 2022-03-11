from click import echo
from flask import Flask, jsonify, render_template, request, redirect, url_for, session 
from flask_mysqldb import MySQL 
from flask_mysqldb import MySQL 
import MySQLdb.cursors 
import re
# from sqlalchemy import create_engine

def init_app() -> Flask:
    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'bdd_projet'

    mysql = MySQL(app) 

#   page d'accueil du site permettant de ce connecter
    @app.route("/accueil", methods =['GET', 'POST'])
    def index():
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form: 
          email = request.form['email'] 
          password = request.form['password'] 
          cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
          cursor.execute('SELECT * FROM employe WHERE Adresse_mail = % s AND Password = % s', (email, password, )) 
          account = cursor.fetchone() 
          if account: 
            msg = "ça fonctionne ma gueule"
            return render_template('login.html', msg = msg) 
          else: 
            print("ça fonctionne pas du con")
        return render_template('index.html')

#   page d'inscription du site
    @app.route("/inscription")
    def inscription():
        return render_template('inscription.html')

#   page de questionnaire du site avec toute les questions
    @app.route("/questionnaire")
    def questionnaire():
        return render_template('questionnaire.html')

    return app
