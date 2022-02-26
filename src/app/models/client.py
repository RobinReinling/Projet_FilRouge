# coding: utf-8
from sqlalchemy import Table
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.INTEGER, primary_key=True)
    nom = db.Column(db.String(200))
    prenom = db.Column(db.String(200))
    commandes = db.relationship(
        "Commande", cascade="all, delete", passive_deletes=True)

    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return f'<Client nom:{self.nom} prenom:{self.prenom}>'

    def __getstate__(self):
        state = self.__dict__.copy()
        print(state)
        del state['_sa_instance_state']
        return state
