from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
from app.models.moon import Moon

# creates planet blueprint
planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
moons_bp = Blueprint("moons", __name__, url_prefix = "/moons")

# HELPER FUNCTION to validate planet by id
def validate_model(cls,model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"planet {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

def filter_by_queries():
    pass
    # possible queries to filter by
    # name_query = request.args.get("name")
    # moons_query = request.args.get("moons")
    # description_query = request.args.get("description")
    
    # if name_query:
    #     planet = Planet.query.filter_by(name=name_query)
    # elif moons_query:
    #     planet = Planet.query.filter_by(moons=moons_query)
    # elif description_query:
    #     planet = Planet.query.filter_by(description=description_query)
    
    ### FEATURE IN PROGRESS ###
    # # creates a query list and remove all None values
    # query_results=[name_query, moons_query, description_query]
    # for query in query_results:
    #     if not query:
    #         query_results.remove(None)

    # # creates a list of planet_results to append all planet instances found to it
    # planet_results=[]
    # if query_results:
    #     for query in query_results:
    #         if name_query:
    #             planet_results.append(planet = Planet.query.filter_by(name=name_query))
    #         elif moons_query:
    #             planet_results.append(planet = Planet.query.filter_by(moons=moons_query))
    #         elif description_query:
    #             planet_results.append(planet=Planet.query.filter_by(description=description_query))
    #     # creates a set to return a set of unique planet instances
    #     planets = set(planet_results)
    # else:
    #     planets = Planet.query.all()

    # return planets
    

# CREATE NEW PLANET - POST
@planets_bp.route("", methods=['POST'])
def create_planet():
    request_body = request.get_json()
    
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()
    
    return jsonify(f"Yay Planet {new_planet.name} successfully created!"), 201 

# READ ONE PLANET BY ID - GET
@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet,planet_id)
    return planet.to_dict(), 200

# READ ALL PLANETS - GET
@planets_bp.route("", methods=['GET'])
def read_all_planets():
    planets_response = []
    name_query = request.args.get("name")
    moons_query = request.args.get("num_moons")
    description_query = request.args.get("description")

    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    elif moons_query:
        planets = Planet.query.filter_by(moons=moons_query)
    elif description_query:
        planets = Planet.query.filter_by(description=description_query)
    else:
        planets = Planet.query.all()
    
    # activate once 'filter_by_queries()' helper feature is complete
    # planets = filter_by_queries()
    
    for planet in planets:
        planets_response.append(planet.to_dict())
        
    return jsonify(planets_response)

# UPDATE ONE PLANET BY ID - PUT
@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moons = request_body["num_moons"]

    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully updated")

# DELETE ONE PLANET BY ID - DELETE
@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"planet #{planet.id} successfully deleted")

### Moons ###
# POST METHOD - create a moon
@moons_bp.route("", methods=["POST"])
def create_moon():
    request_body = request.get_json()

    new_moon = Moon(
        name = request_body["name"]
    )

    db.session.add(new_moon)
    db.session.commit()

    return jsonify(f"Yayyyy Moon {new_moon.name} successfully created!"), 201

# GET METHOD - read all moons
@moons_bp.route("", methods = ["GET"])
def read_all_moons():
    moons_response = []
    moons = Moon.query.all()

    for moon in moons:
        moons_response.append({"id": moon.id, "name": moon.name, "planet":moon.planet.name})
    
    return jsonify(moons_response)

# GET METHOD - read moon by moon_id
@moons_bp.route("/<moon_id>", methods = ["GET"])
def read_moon_by_id(moon_id):
    moon = validate_model(Moon, moon_id)

    return {
        "id": moon.id,
        "name": moon.name,
        "planet": moon.planet.name
    }, 200

# PUT METHOD
@moons_bp.route("/<moon_id>", methods = ["PUT"])
def update_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    request_body = request.get_json()

    moon.name = request_body["name"]
    moon.planet.name = request_body["name"]
    
    db.session.commit()

    return {
        "id" : moon.id,
        "name": moon.name,
        "planet": moon.planet.name
    }, 200

# DELETE METHOD
@moons_bp.route("/<moon_id>", methods = ["DELETE"])
def delete_moon(moon_id):
    moon = validate_model(Moon, moon_id)

    db.session.delete(moon)
    db.session.commit()

    return make_response(f"Moon #{moon_id} successfully deleted")

# POST METHOD - create a moon given a planet_id

# GET METHOD - read all moons given a planet_id