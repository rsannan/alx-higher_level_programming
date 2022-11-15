#!/usr/bin/node
// writes a string to a file.

const fs = require('fs');
const myArgs = process.argv.slice(2);
const path = myArgs[0];

const data = myArgs[1];
fs.writeFile(path, data, (err) => {
  if (err) { console.log(err); }
});
