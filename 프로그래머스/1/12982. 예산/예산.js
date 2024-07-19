function solution(d, budget) {
    d = d.sort((a, b) => a - b);
    let cnt = 0;
    let total = 0;
    while (d[cnt] + total <= budget ){
        total += d[cnt];
        cnt++;
    }
    return cnt;
}