#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
  console.log('Missing number occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
