# test 1 = get all the planets but we want it to be empty
# clean database
def test_read_all_planets_return_empty_list(client):
    # arrange
    # does not need to be used
    # act
    # gets us access to all the methods
    response = client.get("/planets")
    response_body = response.get_json()
    # assert
    # check to make sure the list is empty
    assert response_body == []
    # check the status code of the response - successful request because the resources was found
    assert response.status_code == 200

# test 2    
def test_read_planet_by_id(client, make_two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()
    
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "Really really small and abandoned.",
        "moons": 5
    }
    
def test_create_planet(client):
    response = client.post("/planets", json={
        "name" : "Mercury",
        "description": "Fast around the sun, the smallest of the milky way. It's also a rocky one.",
        "moons": 0
    })
    
    # get the json from the response
    response_body = response.get_json()
    # check for status code and response body is a successfully created message
    assert response.status_code == 201
    # if we did not return a json then it returns none
    #
    assert response_body == "Yay Planet Mercury successfully created!"