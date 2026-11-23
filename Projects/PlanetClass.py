class Planet():
    def __init__(self, name, planet_type,star):
        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        if not isinstance(name, str):
            raise TypeError("name, planet type, and star must be strings")
        if not isinstance(planet_type, str):
            raise TypeError("name, planet type, and star must be strings") 
        if not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")
        self.name = name
        self.planet_type = planet_type
        self.star = star
    def orbit(self):
        return(f"{self.name} is orbiting around {self.star}...")
    def __str__(self):
        return(f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}")

Planet1 = Planet("Earth", "Rock", "Sun")
Planet2 = Planet("Pluto", "Gas", "Sun")
Planet3 = Planet("Gloazorpzorp", "Unknown", "Ziggle")


print(Planet1)
print(Planet2)
print(Planet3)