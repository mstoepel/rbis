from unittest import TestCase
from simulation.systems.planet import Planet, Resource, Iron

class TestPlanet(TestCase):

    def test_distance(self):
        planet1 = Planet('planet1', 'alpha', 100, 2000, 50, 100)
        planet2 = Planet('planet2', 'alpha', 50, 1000, 50, 90)
        self.assertEqual(planet1.distance(planet2), 10)

    def test_exception(self):
        planet1 = Planet('planet1', 'alpha', 100, 2000, 50, 100)
        planet3 = Planet('planet3', 'beta', 200, 1500, 20, 100)
        self.assertRaises(ValueError, planet1.distance, planet3)

    def test_add_supply(self):
        planet1 = Planet('planet1', 'alpha', 100, 2000, 50, 100)
        iron = Resource('iron', planet1, 100, 0.5, 10, 20)
        iron.add_supply(20)
        iron.add_supply(50)
        self.assertEqual(planet1.contains[iron], 170)

    def test_remove_supply(self):
        planet1 = Planet('planet1', 'alpha', 100, 2000, 50, 100)
        iron = Iron('iron', planet1, 100, 0.5, 10, 20)
        iron.remove_supply(150)
        self.assertEqual(iron.amount, 0)

    def test_update(self):
        planet1 = Planet('planet1', 'alpha', 100, 2000, 50, 100)
        planet1.update(5)
        self.assertIn(planet1.wealth, [-3000, 7000])