# coding: utf-8
from sqlalchemy import Table
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produit(db.Model):
    """
        Un model est un objet de la vie réelle (dépendant du projet).
        Les données seront enregistrées dans une base de données, et dans ce cas, le modèle est parfois appelé entité.
    """
    # nom de la table dans la bdd
    __tablename__ = 'produit'
    # liste des champs et des relations de la table dans la BDD
    id = db.Column(db.INTEGER, primary_key=True)
    nom = db.Column(db.String(200))
    prix = db.Column(db.DECIMAL(10, 0))
