#!/usr/bin/node
let p;
if (process.argv.length <= 2) {
  p = 'No argument';
} else if (process.argv.length === 3) {
  p = 'Argument found';
} else {
  p = 'Arguments found';
}
console.log(p);
