#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movie = JSON.parse(body);
  if (movie.episode_id === movieId) {
    console.log(movie.title);
  } else {
    console.log(`No movie found with episode id ${movieId}`);
  }
});
