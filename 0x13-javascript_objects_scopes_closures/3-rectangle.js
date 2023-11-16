#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
      if (!Number.isInteger(w) || w <= 0 || !Number.isInteger(h) || h <= 0) {
        return `${this.constructor.name} {}`;
      }
      this.width = w;
      this.height = h;
    }

    print() {
        i = 0;
        while (i < this.height) {
            console.log('X'.repeat(this.width));
        }
    }
  }
  
  module.exports = Rectangle;
  