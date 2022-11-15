#!/usr/bin/node
// prints the title of a Star Wars movie
// where the episode number matches a given integer

const request = require('request');
const myArgs = process.argv.slice(2);

const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
