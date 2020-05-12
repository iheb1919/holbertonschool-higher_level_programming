#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, body, response) {
  if (error) {
    console.error('error:', error);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], response, 'utf-8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
