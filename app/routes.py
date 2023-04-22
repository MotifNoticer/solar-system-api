from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

#create a list of Planets
planets = [
    Planet (1, "Mars", "We're still looking for water here"),
    Planet(9, "Saturn", "Maybe it's kind of yellow"),
    Planet (5, "Pluto", "Basically the forgotten middle child of Planets")
]

# creates planet blueprint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])

# define the function to handle the planets
# creates list of planets
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        })
    return jsonify(planets_response)

# if given a planet instance that doesn't exist,
# return error message 404
def read_planet(planet):
    for planet in planets:
        if planet not in planets:
            return {
                "error404" : "Planet not found"
                }
        return {
            "id": planet.id,
            "title": planet.title,
            "description": planet.description
        }

# if given a planet_id instance that doesn't exist,
# return error message 400
def read_planet_by_id(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet_id == planet.id:
            return {
        "id": planet.id,
        "title": planet.title,
        "description": planet.description
    }
    return {
            "error400" : "planet_id is invalid"
            }

