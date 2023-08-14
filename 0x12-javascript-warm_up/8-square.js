#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let u = 0; u < x; u++) {
    let y = 0;
    let myVar = '';

    while (y < x) {
      myVar = myVar + 'X';
      y++;
    }
    console.log(myVar);
  }
}
