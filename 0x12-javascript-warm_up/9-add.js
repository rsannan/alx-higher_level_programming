#!/usr/bin/node
const myArgs = process.argv.slice(2);
function add (a, b) {
  const numA = Number(a);
  const numB = Number(b);
  console.log(numA + numB);
}
add(myArgs[0], myArgs[1]);
