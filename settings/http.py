from flask import Flask
import routes

def create_app():
    app = Flask(__name__)

    #routes mapping
    app.register_blueprint(routes.insertion.bp)
    app.register_blueprint(routes.updation.bp)
    app.register_blueprint(routes.deletion.bp)
    return app
