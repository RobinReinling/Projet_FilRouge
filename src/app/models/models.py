# coding: utf-8
from sqlalchemy import Table
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Client(db.Model):
    """
    Un model est un objet de la vie réelle dont les données seront enregistrées
    dans une base de données.
    """
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


class Produit(db.Model):
    __tablename__ = 'produit'

    id = db.Column(db.INTEGER, primary_key=True)
    nom = db.Column(db.String(200))
    prix = db.Column(db.DECIMAL(10, 0))


class Commande(db.Model):
    __tablename__ = 'commande'

    id = db.Column(db.INTEGER, primary_key=True)
    date = db.Column(db.Date, server_default=db.text("current_timestamp()"))
    client_id = db.Column(db.ForeignKey(
        'client.id', ondelete='cascade'), nullable=False, index=True)

    client = db.relationship('Client')
    produits = db.relationship('Produit', secondary='contenir')


t_contenir = db.Table(
    'contenir',
    db.Column('commande_id', db.ForeignKey(
        'commande.id'), nullable=False, index=True),
    db.Column('produit_id', db.ForeignKey(
        'produit.id'), nullable=False, index=True)
)
