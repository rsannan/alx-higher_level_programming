#!/usr/bin/node
// display the status code of a GET request

const request = require('request');
const myArgs = process.argv.slice(2);

request(myArgs[0], function (err, response, body) {
  if (err) { console.error(err); }
  console.log('code:', response.statusCode);
});
