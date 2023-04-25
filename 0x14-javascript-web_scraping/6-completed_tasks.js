#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
// let counTrue = 0;
// let userId = 1;
const object = {};
request(apiUrl, function (err, resp, body) {
  if (resp.statusCode === 200) {
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (object[task.userId]) {
          object[task.userId]++;
        } else {
          object[task.userId] = 1;
        }
      }
    }
  } else {
    console.log(err);
  }
  console.log(object);
});
