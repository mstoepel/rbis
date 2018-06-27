class Ship {
  static restore({ system, x, y, contains, speed, destination }) {
    return new Ship(system, x, y, contains, speed, destination);
  }

  constructor(system, x, y, contains, speed, destination) {
    this.system = system;
    this.x = x;
    this.y = y;
    this.contains = contains;
    this.speed = speed;
    this.destination = destination;
  }

  toJSON() {
    let { system, x, y, contains, speed, destination } = this;
    return {
      x,
      y,
      contains,
      speed,
      destination
    }
  }
}

if (!window.simulation) {
  window.simulation = {};
}

window.simulation.ship = {
  'Ship': Ship
};