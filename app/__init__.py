from flask import Flask

def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # import routes
    from .routes import planets_bp, planet_id_bp
    # register the blueprint
    app.register_blueprint(planets_bp)
    app.register_blueprint(planet_id_bp)

    return app

