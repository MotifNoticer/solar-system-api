from flask import Flask

def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # import routes
    from .routes import planets_bp
    # register the blueprint
    app.register_blueprint(planets_bp)

    return app

