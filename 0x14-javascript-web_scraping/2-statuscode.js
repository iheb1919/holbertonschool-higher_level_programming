#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response) {
  if (error) {
    console.log('error:', error);
  } else {
      console.log('Code:', response.statusCode);
  }
});
