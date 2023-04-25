from flask import Blueprint, jsonify, abort, make_response
class Planet:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

# create helper function whose single responsibility is to validate id passed in and reurn the instance of the planet that is found
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"{planet_id} is not a valid data type. A {type(planet_id)} data type was provided. A valid integer must be provided."},400))
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message:" : f"planet {planet_id} does not exist"},404))

#create a list of Planets
planets = [
    Planet (1, "Mars", "We're still looking for water here"),
    Planet(9, "Saturn", "Maybe it's kind of yellow"),
    Planet (5, "Pluto", "Basically the forgotten middle child of Planets")
]

# creates planet blueprint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# decorator to accept following inputs
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

@planets_bp.route("/<planet_id>", methods=["GET"])
# if given a planet instance that doesn't exist,
# return error message 404
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "title": planet.title,
        "description": planet.description
    }



