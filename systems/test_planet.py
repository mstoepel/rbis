from unittest import TestCase
from systems.planet import Planet, Resource

class TestPlanet(TestCase):

    def test_distance(self):
        planet1 = Planet('alpha', 100, 2000, 50, 100)
        planet2 = Planet('alpha', 50, 1000, 50, 90)
        self.assertEqual(planet1.distance(planet2), 10)

    def test_exception(self):
        planet1 = Planet('alpha', 100, 2000, 50, 100)
        planet3 = Planet('beta', 200, 1500, 20, 100)
        self.assertRaises(ValueError, planet1.distance, planet3)

    def test_add_good(self):
        iron = Resource('iron', 'planet1', 100, 0.5, 10, 20)
        iron.add_good(20)
        self.assertEqual(iron.amount, 120)