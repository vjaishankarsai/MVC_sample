from flask import Flask
import routes

def create_app():
    app = Flask(__name__)

    #routes mapping
    app.register_blueprint(routes.insertion.bp)
    return app
