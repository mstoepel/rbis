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


# p1 =  Planet('alpha', 100000, 2000000, 50, 100)
# pl2 = Planet('alpha', 50000, 100000, 20, 200)
#
# dist = p1.distance(pl2)
# print(dist)