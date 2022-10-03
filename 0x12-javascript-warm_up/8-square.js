#!/usr/bin/node
const myVar = process.argv.slice(2);
const num = Number(myVar[0]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let str = '';
    for (let j = 0; j < num; j++) {
      str = str + 'X';
    }
    console.log(str);
  }
}
