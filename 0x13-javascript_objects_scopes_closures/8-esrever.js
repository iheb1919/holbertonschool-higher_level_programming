#!/usr/bin/node
// reverse a list

exports.esrever = function (list) {
  const lis2 = [];
  for (let i = list.length; i > -1; i--) {
    lis2.push(list[i]);
  }
  return lis2;
};
