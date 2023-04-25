#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, function (err, resp, body) {
  if (resp.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', function (err, data) {
      if (err) return console.log(err);
    });
  } else {
    console.error(err);
  }
});
