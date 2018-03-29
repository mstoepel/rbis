from systems.planet import Planet, Resource, Iron, Water
from systems.system import SolarSystem


planet1 = Planet('planet1', 'alpha', 1000, 20000, 50, 50)
planet2 = Planet('planet2', 'alpha', 2000, 30000, 40, 60)

iron1 = Iron('iron', planet1, 500, 0.5, 20, 20)
iron2 = Iron('iron', planet2, 1000, 0.5, 30, 30)
iron3 = Iron('iron', planet2, 50, 0.5, 40, 45)

water1 = Water('water', planet1, 5000, 0.9, 10, 10)
water2 = Water('water', planet2, 2000, 0.9, 20, 20)
water3 = Water('water', planet2, 500, 0.9, 30, 35)

alpha = SolarSystem('alpha')
alpha.add_planet([planet1, planet2])

print(Iron.registry[0].total)
print(Water.registry[0].total)

print(planet1.contains)
print(planet2.contains)

print(alpha.planets)