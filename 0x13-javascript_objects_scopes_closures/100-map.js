#!/usr/bin/node
// map

const listt = require('./100-data').list;
console.log(listt);
console.log(listt.map((x, i) => x * i));