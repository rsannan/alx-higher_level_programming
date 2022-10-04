#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let l = 0; l < this.width; l++) {
        str += c;
      }
      console.log(str);
    }
  }
};
