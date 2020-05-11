#!/usr/bin/node
// map

const list1 = require('./100-data').list;
console.log(list1);
console.log(list1.map((x, i) => x * i));
