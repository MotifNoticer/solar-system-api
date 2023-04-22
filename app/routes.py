from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

#create a list of Planets instances
planets = [
    Planet (1, "Mars", "We're still looking for water here"),
    Planet(9, "Saturn", "Maybe it's kind of yellow"),
    Planet (5, "Pluto", "Basically the forgotten middle child of Planets")
]

# creates planet blueprint
planets_bp = Blueprint("books", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])

#define the function to handle the planets
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        })
    return jsonify(planets_response)
