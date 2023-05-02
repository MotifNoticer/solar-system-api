from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet

# creates planet blueprint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# HELPER FUNCTION to validate planet by id
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet

# CREATE NEW PLANET - POST
@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    
    new_planet = Planet(
        name = request_body['name'],
        description = request_body['description'],
        moons = request_body['moons']
    )

    db.session.add(new_planet)
    db.session.commit()
    
    return make_response(f"Yay Planet {new_planet.name} successfully created!", 201) 

# READ ONE PLANET BY ID - GET
@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        }

# READ ALL PLANETS - GET
@planets_bp.route("", methods=['GET'])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons
        })
        
    return jsonify(planets_response)

# UPDATE ONE PLANET BY ID - PUT
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["moons"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

# DELETE ONE PLANET BY ID - DELETE
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"planet #{planet.id} successfully deleted")