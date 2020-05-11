#!/usr/bin/node

const dict1 = require('./101-data').dict;
const dict2 = {};
for (const k in dict1) {
  if (dict2[dict1[k]] === undefined) {
    dict2[dict1[k]] = [];
  }
  dict2[dict1[k]].push(k);
}
console.log(dict2);