#!/usr/bin/node
const args = process.argv.slice(2);
const num = Number(args[0]);

function factorial(num) {
    if (num === 'NaN' || num === 0 || num === 1) {
        return (1);
    }
    return (num * factorial(num - 1));
}

const res = factorial(num);
console.log(res);