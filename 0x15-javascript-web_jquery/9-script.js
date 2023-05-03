const $ = require('jquery');

$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    const greeting = data.hello;
    $('#hello').text(greeting);
  });
});
