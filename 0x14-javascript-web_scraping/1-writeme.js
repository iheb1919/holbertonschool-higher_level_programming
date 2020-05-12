#!/usr/bin/node

var fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3] + '\n', 'utf-8',
	     function (error) {
    if (error) {
	console.log(error);
    }
});
