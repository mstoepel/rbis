import math
import random


class Ship:
    def __init__(self, system, x, y, speed=10):

        self.system = system
        self.x = x
        self.y = y
        self.speed = speed

        self.destination = None
        self.system.register_ship(self)

    def change_system(self, new_system):
        self.system.unregister_ship(self)
        self.system = new_system
        self.system.register_ship(self)

    def update(self, dt):
        if not self.destination:
            self.destination = random.choice(self.system.planets)

        direction = (self.destination.x - self.x, self.destination.y - self.y)
        distance = math.sqrt(direction[0] * direction[0] + direction[1] * direction[1])

        if distance:
            dx, dy = (direction[0] / distance * self.speed * dt, direction[1] / distance * self.speed * dt)

            if abs(dx) > abs(direction[0]):
                dx = direction[0]

            if abs(dy) > abs(direction[1]):
                dy = direction[1]

            self.x += dx
            self.y += dy

        if self.x == self.destination.x and self.y == self.destination.y:
            self.destination = None
