#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const num = args.map(Number);
  const sorNum = num.sort((a, b) => a - b);
  console.log(sorNum[sorNum.length - 2]);
}
