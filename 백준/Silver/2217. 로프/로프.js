var input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
//var input = require("fs").readFileSync("example.txt").toString().split("\n");

let inputToNum = input.map((x) => parseInt(x));
n = inputToNum[0];
let lopeInfo = inputToNum.slice(1);
lopeInfo = lopeInfo.sort((a, b) => b - a);

let maxWeight = 0;

for (let i = 0; i < n; i++) {
  let weight = lopeInfo[i] * (i + 1);
  if (weight > maxWeight) maxWeight = weight;
}

console.log(maxWeight);
