from flask import Flask, render_template,jsonify
# from sqlalchemy import create_engine

def init_app() -> Flask:
    app = Flask(__name__)


    @app.route("/")
    def index():
        return render_template('index.html')
    
    return app
