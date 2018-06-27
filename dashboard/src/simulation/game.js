class Game {
  static restore(obj) {
    const { objects, running } = obj['py/state'];
    return new Game(objects, running);
  }

  constructor(objects, running) {
    this.objects = objects;
    this.running = running;
  }

  toJSON() {
    const {objects, running} = this;
    return {
      objects,
      running
    }
  }
}

window.game = { 'Game': Game };