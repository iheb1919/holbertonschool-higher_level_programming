#!/usr/bin/node
// status of a request
const myRequest = require('request');
const myUrl = process.argv[2];
myRequest(myUrl, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    let c = 0;
    const json = JSON.parse(body).results;
    for (let i = 0; i < json.length; i++) {
      const chars = json[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].search('/18') > 0) {
          c++;
        }
      }
    }
    console.log(c);
  }
});
