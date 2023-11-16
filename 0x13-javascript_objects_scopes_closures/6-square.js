#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
    constructor() {
        super();
    }

    charPrint(c) {
        let char = c;
        if (char === undefined) {
            const x_print = super.print();
        } else {
            let i = 0;
            while (i < this.height) {
                console.log(char.repeat(this.width));
                i++;
            }
        }
    }
}