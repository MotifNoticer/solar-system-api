from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    num_moons = db.Column(db.Integer)
    moons = db.relationship("Moon", back_populates = "planet")
    

    @classmethod
    def from_dict(cls,planet_data):
        new_planet = Planet(
            name = planet_data["name"],
            description = planet_data["description"],
            num_moons = planet_data["moons"]
        )
        return new_planet
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "number of moons": self.moons
        }