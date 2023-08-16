#!/usr/bin/node

const PrevSquare = require('./5-square');

class Square extends PrevSquare {
  charPrint (c) {
    const myChar = c === undefined ? 'X' : c;
    for (let a = 0; a < this.height; a++) {
      let myVar = '';
      let y = 0;
      while (y < this.width) {
        myVar += myChar;
        y++;
      }

      console.log(myVar);
    }
  }
}

module.exports = Square;
