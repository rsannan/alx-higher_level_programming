#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length <= 1) {
  console.log(0);
} else {
  const newArg = myArgs.map(Number);
  newArg.sort(function (a, b) { return a - b; });
  console.log(newArg[newArg.length - 2]);
}
