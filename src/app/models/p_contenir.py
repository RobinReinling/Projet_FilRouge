# coding: utf-8
from sqlalchemy import Table
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

t_contenir = db.Table(
    'contenir',
    db.Column('commande_id', db.ForeignKey(
        'commande.id'), nullable=False, index=True),
    db.Column('produit_id', db.ForeignKey(
        'produit.id'), nullable=False, index=True)
)
