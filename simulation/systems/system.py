from simulation.systems import Planet


class SolarSystem:
    def __init__(self, name):
        self.planets = []
        self.ships = []
        self.name = name

    def add_planet(self, planet):
        # self.planets.append(planets)
        # for planet in planets:
        # setattr(self, planet.name, planet)
        self.planets.append(planet)

    def register_ship(self, ship):
        self.ships.append(ship)

    def unregister_ship(self, ship):
        self.ships.remove(ship)

    def update(self, dt):
        for planet in self.planets:
            planet.update(dt)