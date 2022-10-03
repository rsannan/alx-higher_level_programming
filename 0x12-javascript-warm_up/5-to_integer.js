#!/usr/bin/node
const myVar = process.argv.slice(2);
const num = Number(myVar[0]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
