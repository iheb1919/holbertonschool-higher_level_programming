#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/';
const request = require('request');
request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
