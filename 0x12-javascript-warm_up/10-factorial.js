#!/usr/bin/node
const args = process.argv.slice(2);
const num = Number(args[0]);

function factorial (num) {
  if (isNaN(num) || num === 0 || num === 1) {
	  return (1);
  } else {
	  return (num * factorial(num - 1));
  }
}

const res = factorial(num);
console.log(res);
