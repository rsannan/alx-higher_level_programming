#!/usr/bin/node
const myVar = process.argv.slice(2);
const num = Number(myVar[0]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
