def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    ids = {
        "1": "Mercury",
        "2": "Venus",
        "2": "Earth",
        "4": "Mars",
        "5": "Jupiter",
        "6": "Saturn",
        "7": "Uranus" , 
        "8": "Neptune"
        }
    name = ids[str(id)]
    return name