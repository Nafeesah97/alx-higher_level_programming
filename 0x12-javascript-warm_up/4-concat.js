#!/usr/bin/node
const args = process.argv.slice(2);

let sentence = args[0].concat(' is');
let newSen = sentence.concat(args[1]);
console.log(newSen);