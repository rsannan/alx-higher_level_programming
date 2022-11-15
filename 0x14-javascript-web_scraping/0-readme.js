#!/usr/bin/node
// reads and prints the content of a file.

const fs = require('fs');
const myArgs = process.argv.slice(2);

fs.readFile(myArgs[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
