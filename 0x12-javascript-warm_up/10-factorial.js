#!/usr/bin/node
const myArgs = process.argv.slice(2);
function factorial (x) {
  let num = Number(x);
  if (isNaN(num)) {
    num = 1;
  }
  if (num === 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(myArgs[0]));
