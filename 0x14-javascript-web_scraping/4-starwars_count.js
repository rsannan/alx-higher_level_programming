#!/usr/bin/node
// prints the number of movies
// where the character “Wedge Antilles” is present

const request = require('request');
const myArgs = process.argv.slice(2);
let count = 0;

request(myArgs[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const allFilms = JSON.parse(body).results;
    for (const film of allFilms) {
      const characters = film.characters;
      for (const val of characters) {
        if (val.includes('18')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
