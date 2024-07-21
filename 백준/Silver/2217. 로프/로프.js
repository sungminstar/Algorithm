 var input = require("fs").readFileSync("/dev/stdin").toString().split("\n");
//var input = require("fs").readFileSync("example.txt").toString().split("\n");

// 입력 데이터 처리
let inputToNum = input.map((x) => parseInt(x));
let n = inputToNum[0]; // 첫 번째 요소는 로프의 개수
let lopeInfo = inputToNum.slice(1); // 나머지는 로프의 중량 정보

// 로프 중량 정보를 내림차순으로 정렬
lopeInfo.sort((a, b) => b - a);

let maxWeight = 0;

// 로프 개수를 하나씩 늘려가며 최대 중량 계산
for (let i = 0; i < n; i++) {
  // i개의 로프를 사용할 때 들어올릴 수 있는 최대 중량
  let weight = lopeInfo[i] * (i + 1);
  if (weight > maxWeight) {
    maxWeight = weight;
  }
}

console.log(maxWeight);
