function solution(left, right) {
    let result_sum = 0;
    for (let i = left; i <= right; i++){
        let cnt = 0;
        for (let j = 1; j <= i; j++) {
            i % j === 0 ? cnt += 1 : cnt;
        }
        cnt % 2 === 0 ? result_sum += i : result_sum -= i;
    }
    return result_sum;
}