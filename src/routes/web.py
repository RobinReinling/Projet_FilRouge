from flask import jsonify, render_template, Blueprint
from src.models import models
from src.models.models import Client

web_routes = Blueprint('web', __name__)

@web_routes.route('/accueil', methods=['GET'])
def accueil():
    return render_template('index.html')

@web_routes.route('/clients', methods=['GET'])
def clients():
    return render_template('clients.html')   

@web_routes.route('/produits', methods=['GET'])
def produits():
    return render_template('produits.html') 

@web_routes.route('/mathematiques', methods=['GET'])
def mathematiques():
    return render_template('mathematiques.html')    

@web_routes.route('/test', methods=['GET'])
def tests():
    clients = Client.query.all()
    result = []
    for e in clients:
        result.append(e.__repr__())
    return jsonify(result), 200    

@web_routes.route('/commandes', methods=['GET'])
def commandes():
    return render_template('commandes.html', prenom='Robin', mes_commandes=["sucre","chocolat","cacao"])  