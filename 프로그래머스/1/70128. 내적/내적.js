function solution(a, b) {
    let inner = 0;
    for (let i = 0; i < a.length; i++) {
        inner += a[i] * b[i]
    }
    return inner;
}