#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const myArgs = process.argv.slice(2);
const request = require('request');
const fs = require('fs');

request(myArgs[0], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(myArgs[1], body, {
    encoding: 'utf8',
    flag: 'w'
  }, err => {
    if (err) {
      console.log(err);
    }
  });
});
