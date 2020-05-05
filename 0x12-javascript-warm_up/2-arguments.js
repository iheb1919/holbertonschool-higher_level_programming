#!/usr/bin/node
if (process.argv.length <= 2) {
    p = ' No Arguments';}
else if (process.argv.length <= 3) {
    p = 'Arguments found';}
else {
    p = 'Arguments founds';}
console.log(p);
