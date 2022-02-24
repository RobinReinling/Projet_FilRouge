from flask import Flask
import src.routes.web as web
import src.routes.mathematiques as math

def charger_routes(app: Flask) -> None:

    "Permet de charger l'ensemble des routes sur une application Flask Args: "
    "app (Flask): Application Flask sur laquelle nous voulons ajouter des routes"

    app.register_blueprint(web.web_routes)
    app.register_blueprint(math.routes)


def init_app() -> Flask:

    "on crée une application Flask Returns: Flask: application Flask avec les routes "
    app = Flask(__name__, template_folder='templates')
# fonction qui charge l'ensemble des routes de notre serveur
    charger_routes(app)
    return app
