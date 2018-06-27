class SolarSystem {
  static restore({ planets, ships }) {
    return new SolarSystem(planets, ships);
  }

  constructor(planets, ships) {
    this.planets = planets;
    this.ships = ships;
  }

  toJSON() {
    let { planets, ships } = this;
    return {
      planets,
      ships
    }
  }
}

class Planet {
  static restore({ system, pop, wealth, x, y }) {
    return new Planet(system, pop, wealth, x, y);
  }

  constructor(system, pop, wealth, x, y) {
    this.system = system;
    this.pop = pop;
    this.wealth = wealth;
    this.x = x;
    this.y = y;
  }

  toJSON() {
    let { system, pop, wealth, x, y } = this;
    return {
      pop,
      wealth,
      x,
      y
    }
  }
}

if(!window.simulation) {
  window.simulation = {};
}

window.simulation.systems = {
  system: {
    'SolarSystem': SolarSystem
  },
  planet: {
    'Planet': Planet
  }
};