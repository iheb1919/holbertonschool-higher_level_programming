#!/usr/bin/node
if (process.argv.length < 1) {
    p = "No Argument";}
else if (process.argv.length < 2) {
    p = "Argument found";}
else {
    p = "Arguments found";}
console.log(p);
