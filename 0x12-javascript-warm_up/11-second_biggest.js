#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv
    .map(Number)
    .slice(2, process.argv.length)
    .sort((i, u) => i - u);
  console.log(args[args.length - 2]);
}
