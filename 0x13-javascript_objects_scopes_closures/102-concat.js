#!/usr/bin/node
let i = 2;
while (i <= 3) {
  const fs = require('fs');
  fs.readFile(process.argv[i], (err, data) => {
    if (err) throw err;
    fs.appendFile(process.argv[4], data, (err) => {
      if (err) throw err;
    });
  });
  i++;
}
