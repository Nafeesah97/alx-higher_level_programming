#!/usr/bin/node
const args = process.argv.slice(2);
const num1 = Number(args[0]);
const num2 = Number(args[1]);

function add (a, b) {
  return (a + b);
}

const res = add(num1, num2);
console.log(res);
