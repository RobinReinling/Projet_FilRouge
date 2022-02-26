# coding: utf-8
from sqlalchemy import Table
from flask_sqlalchemy import SQLAlchemy
from . import p_contenir

db = SQLAlchemy()

class Commande(db.Model):
    __tablename__ = 'commande'

    id = db.Column(db.INTEGER, primary_key=True)
    date = db.Column(db.Date, server_default=db.text("current_timestamp()"))
    client_id = db.Column(db.ForeignKey(
        'client.id', ondelete='cascade'), nullable=False, index=True)

    client = db.relationship('Client')
    produits = db.relationship('Produit', secondary='contenir')
