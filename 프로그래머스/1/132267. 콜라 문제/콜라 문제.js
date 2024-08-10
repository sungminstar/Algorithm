function solution(a, b, n) {
    // 20 -> (6) 6+2 => (2) 2 + 2 (1) 1 + 1
    var answer = 0;
    while(n >= a) {
        answer += Math.floor(n / a) * b;
        n = Math.floor(n / a) * b + Math.floor(n % a);
    }
    return answer;
}