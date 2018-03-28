from systems.planet import Planet

class SolarSystem:
    def __init__(self, name):
        self.planets = []
        self.ships = []
        self.name = name

    def add_planet(self, pop, wealth, x, y):
        self.planets.append(Planet(self.name, pop, wealth, x, y))

    def register_ship(self, ship):
        self.ships.append(ship)

    def unregister_ship(self, ship):
        self.ships.remove(ship)

    def update(self, dt):
        for planet in self.planets:
            planet.update(dt)