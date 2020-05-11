#!/usr/bin/node
// number arguments
let num = 0;
exports.logMe = function (item) {
  console.log(`${num}: ${item}`);
  num = num + 1;
};