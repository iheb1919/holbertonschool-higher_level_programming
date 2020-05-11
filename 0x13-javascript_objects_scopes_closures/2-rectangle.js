#!/usr/bin/node
// Class Rectangle
class Rectangle {
  constructor (h, w) {
    if ((w && h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
