from flask import Blueprint, request, jsonify
routes = Blueprint('api_math', __name__)
path = "/api/mathematiques"


@routes.route( f"{path}/addition", methods=['GET'])
def addition():
    # args.get permet de récupèrer la valeur dont le "name" est a du formulaire
    p_a = request.args.get('a')
    p_b = request.args.get('b')
    # p_a et p_b sont considérés comme des string, nous les transformons en float.
    resultat = float(p_a) + float(p_b)
    return f"resultat: {resultat}", 200

@routes.route( f"{path}/multiplication/<pa>/<pb>", methods=['GET'])
def multiplication(pa:float, pb: float):
    # pa et pb sont considérés comme des string, nous les transformons en float.
    resultat = float(pa) * float(pb)
    return f"resultat: {resultat}", 200
    
@routes.route( f"{path}/division", methods=['GET'])
def division():
    # permet de récupérer le contenu s'il est au format JSON
    contenu = request.json
    resultat = contenu['a'] / contenu['b']
    # retourne un résultat au format JSON
    return jsonify({"res": resultat}), 200
