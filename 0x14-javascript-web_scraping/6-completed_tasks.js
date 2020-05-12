#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
let c = 0;
const mydict = {};
request(args[0], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    let userid = body[0].userId;
    for (let i = 0; i < body.length; i++) {
      console.log(body[i].userId);
      if (userid !== body[i].userId) {
        mydict[userid.toString()] = c;
        userid = body[i].userId;
        c = 0;
      } else if
      (body[i].completed === true) {
        c++;
      }
    }
    mydict[userid.toString()] = c;
    console.log(mydict);
  }
});
