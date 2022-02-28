# from flask import jsonify, render_template, Blueprint
# from src.models import models

# web_routes = Blueprint('web', __name__)

# @web_routes.route('/connexion', methods=['GET'])
# def connexion():
#     return render_template('clients.html')

# @web_routes.route('/inscription', methods=['GET'])
# def inscription():
#     return render_template('commandes.html')   

# @web_routes.route('/inscriptionfini', methods=['PUT'])
# def inscriptionfini():
#     return render_template('index.html')   

# # @web_routes.route('/test', methods=['GET'])
# # def tests():
# #     clients = Client.query.all()
# #     result = []
# #     for e in clients:
# #         result.append(e.__repr__())
# #     return jsonify(result), 200    
