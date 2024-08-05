function BinaryConversion(n){
    let cnt = 0;
    while(n > 2) {
        if(n % 2 == 1) cnt++;
        n = Math.floor(n / 2);
    }
    return cnt;
}

function solution(n) {
    let nCnt = BinaryConversion(n);
    let numCnt;
    while(true) {
        n += 1;
        numCnt = BinaryConversion(n);
        if (nCnt === numCnt) return n;
    }
}