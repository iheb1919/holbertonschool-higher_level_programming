#!/usr/bin/node
const request = require('request');
let c = 0;
const dict = {};
request(process.argv[2], function (error, body, response) {
  if (error) {
    console.error('error:', error);
  } else {
    body = JSON.parse(response);
    let userid = body[0].userId;
    for (let i = 0; i < body.length; i++) {
      if (userid !== body[i].userId) {
        dict[userid.toString()] = c;
        userid = body[i].userId;
        c = 0;
      }
      if (body[i].completed === true) {
        c++;
      }
    }
    dict[userid.toString()] = c;
    console.log(dict);
  }
});
