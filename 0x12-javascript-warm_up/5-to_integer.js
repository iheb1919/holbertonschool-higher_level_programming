#!/usr/bin/node
const number = parseInt(process.argv[1]);
if (!isNaN(number)) {
  console.log('My number: ' + process.argv[1]);
} else {
  console.log('Not a number');
}
