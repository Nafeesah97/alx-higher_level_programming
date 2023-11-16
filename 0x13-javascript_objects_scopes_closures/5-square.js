#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || w <= 0 || !Number.isInteger(h) || h <= 0) {
      return `${this.constructor.name} {}`;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  rotate () {
    const h = this.height;
    const w = this.width;
    this.width = h;
    this.height = w;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;

class Square extends Rectangle {
  constructor (size) {
    if (!Number.isInteger(size) || size <= 0) {
      super();
    } else {
      super(size, size);
    }
  }
}
module.exports = Square;
