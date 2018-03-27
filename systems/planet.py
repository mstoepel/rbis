import math

class Planet:
    def __init__(self, system, pop, wealth, x, y):
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

class Resource:
    def __init__(self, name, planet, amount, demand_coeff, x, y):
        self.name = name
        self.planet = planet
        self.amount = amount
        self.demand_coeff = demand_coeff
        self.x = x
        self.y = y

    def add_good(self, count):
        self.amount += count

    def remove_good(self, count):
        if self.amount > 0:
            if self.amount >= count:
                self.amount -= count
            else:
                self.amount = 0
        else:
            self.amount = 0
