const $ = require('jquery');

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const movies = data.results;
  const list = $('#list_movies');
  $.each(movies, function (i, movie) {
    const item = $('<li>').text(movie.title);
    list.append(item);
  });
});
