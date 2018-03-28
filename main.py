from systems.planet import Planet, Resource, Iron


planet1 = Planet('planet1', 'alpha', 1000, 20000, 50, 50)
planet2 = Planet('planet2', 'alpha', 2000, 30000, 40, 60)

Iron('iron', planet1, 500, 0.5, 20, 20)
Iron('iron', planet2, 1000, 0.5, 30, 30)

Iron.calc_total()
print(Iron.total)


