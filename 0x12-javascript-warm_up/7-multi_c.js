#!/usr/bin/node
const args = process.argv.slice(2);
const word = 'C is fun'
const num = Number(args[0]);
let i = 0;
if (isNaN(num)) {
    console.log('Missing number of occurrences');
  } else {
    while (i < num) {
        console.log(word);
        i++;
    }
}