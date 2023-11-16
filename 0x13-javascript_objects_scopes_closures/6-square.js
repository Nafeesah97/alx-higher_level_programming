#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    const char = c;
    if (char === undefined) {
      super.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(char.repeat(this.width));
        i++;
      }
    }
  }
}

module.exports = Square;
