#!/usr/bin/node
const args = process.argv.slice(2);
const word = 'X';
const num = Number(args[0]);
let i = 0;
let j = 0;
if (isNaN(num)) {
  console.log('Missing size');
} else {
    while (i < num) {
        while (j < num) {
            console.log(word);
            j++;
        }
        console.log('\n');
        i++;
    }
}