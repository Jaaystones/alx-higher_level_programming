#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (error) throw error;

  const films = JSON.parse(body).results;

  const numMoviesWithWedgeAntilles = films.reduce((acc, film) => {
    const hasWedgeAntilles = film.characters.some((characterUrl) => {
      const characterIdMatches = characterUrl.match(/\/(\d+)\/$/);
      return characterIdMatches && characterIdMatches[1] === characterId.toString();
    });
    return acc + hasWedgeAntilles;
  }, 0);

  console.log(`Number of movies with Wedge Antilles: ${numMoviesWithWedgeAntilles}`);
});
