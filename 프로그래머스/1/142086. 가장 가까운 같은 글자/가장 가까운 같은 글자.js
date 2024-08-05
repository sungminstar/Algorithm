function solution(s) {
    let StoArray = s.split("");
    let ans = [-1,];
    let i, j;
    for(i = 1; i < StoArray.length; i++){
        for(j = i - 1; j > 0 ; j--){
            if (StoArray[i] != StoArray[j]) {
                continue;
            }
            else break;
        }
        j === 0 && StoArray[i] != StoArray[j]  ? ans.push(-1) : ans.push(i-j) // 처음 : 재등장
    }
    return ans
}