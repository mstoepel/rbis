import math
import random

class Planet:
    def __init__(self, name, system, pop, wealth, x, y):
        self.name = name
        self.system = system
        self.pop = pop
        self.wealth = wealth
        self.x = x
        self.y = y
        self.contains = {}
        self.demands = {}

    def distance(self, other):
        if self.system != other.system:
            raise ValueError('Planet not in same systems!')

        return math.hypot((self.x - other.x), (self.y - other.y))

    def update(self, dt):
        self.wealth += dt * 1000 if random.random() > 0.5 else dt * -1000

    def __repr__(self):
        return '{}'.format(self.name)

class Population:
    def __init__(self, planet, amount, demographic):
        self.planet = planet
        self.amount = amount
        self.demographic = demographic



class Resource:
    def __init__(self, name, planet, amount, demand_coeff, x, y):
        self.name = name
        self.planet = planet
        self.amount = amount
        self.demand_coeff = demand_coeff
        self.x = x
        self.y = y
        planet.contains[self] = amount

    def add_supply(self, count):
        self.amount += count
        self.planet.contains[self] = self.amount

    def remove_supply(self, count):
        self.amount -= count
        self.amount = max(0, self.amount)

    def __repr__(self):
        return ''.format(self.name)

class Iron(Resource):

    registry = []

    def __init__(self, name, planet, amount, demand_coeff, x, y):
        super().__init__(name, planet, amount, demand_coeff, x, y)

        self.registry.append(self)

    @property
    def total(self):
        return sum([i.amount for i in self.registry])

    def __repr__(self):
        return '{0}: {1}'.format(self.name, self.planet)
