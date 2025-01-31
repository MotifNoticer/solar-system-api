from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import libraries for grabbing environment variables
from dotenv import load_dotenv
# used to read environment variables
import os

# gives use access to database operations
db = SQLAlchemy()
migrate = Migrate()
# load the values from our .env file so the os module to be able to see them
load_dotenv()

def create_app(test_config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

# set up the database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:    
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
        
# connect the db and migrate to our flask app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # import routes
    from .routes import planets_bp, moons_bp
        
    # register the blueprint
    app.register_blueprint(planets_bp)
    app.register_blueprint(moons_bp)
    
    from app.models.planet import Planet
    from app.models.moon import Moon

    return app


