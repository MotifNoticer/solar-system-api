import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def make_two_planets(app):
    planet_1 = Planet(
            name = "Pluto",
            description = "Really really small and abandoned.",
            moons = 5
        )
    planet_2 = Planet(
            name = "Uranus",
            description = "Tilts and orbits a little differently than most.",
            moons = 16
            )

    # populate our database with our two planets
    db.session.add_all([planet_1, planet_2])
    db.session.commit()
