#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
}
console.log(add(process.argv[1], process.argv[2]));
