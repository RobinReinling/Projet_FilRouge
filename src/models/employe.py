# coding: utf-8
from sqlalchemy import Table
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employe(db.Model):
    __tablename__ = 'employe'
    id_employe = db.Column(db.INTEGER, primary_key=True)
    Nom = db.Column(db.String(45))
    Prenom = db.Column(db.String(45))
    Adresse_mail = db.Column(db.String(45))
    Password = db.Column(db.String(45))
    organisation_groupe = db.Column(db.String(45))
    questionnaire_idquestionnaire = db.Column(db.INTEGER)

    def __init__(self, nom,prenom,mail,passwd):
        self.Nom = nom
        self.Prenom = prenom
        self.Adresse_mail = mail
        self.Password = passwd
        self.organisation_groupe = 1
        self.questionnaire_idquestionnaire = 1

    def __repr__(self):
        return f'<Employe nom:{self.Nom} prenom:{self.Prenom}>'

    def __getstate__(self):
        state = self.__dict__.copy()
        print(state)
        del state['_sa_instance_state']
        return state
