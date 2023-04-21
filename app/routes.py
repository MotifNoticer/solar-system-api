from flask import Blueprint

class Planet:
    def __init__(self, id, name, color, powers):
        self.id = id
        self.name = name
        self.color = color
        self.powers = powers

#create a list of Planets

planets = [
    Planet(1, "Amethyst", "Purple", "Infinite knowledge and wisdom"),
    Planet(5, "Tiger's Eye", "Gold", "Confidence"),
    Planet(2, "Sapphire", "Dark Blue", "Peace"),
    Planet(3, "Rose Quartz", "Pink", "Self Love"),
]

planets_bp = Blueprint("books", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])

#define the function to handle the planets
def handle_planets():

    planets_response = []

    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "color": planet.color,
            "powers": planet.powers
        })

    return jsonify(planets_response)
