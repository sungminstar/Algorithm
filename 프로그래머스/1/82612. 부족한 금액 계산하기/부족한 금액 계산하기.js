function solution(price, money, count) {
    return Math.floor(price * count * (1 + count) / 2) - money > 0 ? Math.floor(price * count * (1 + count) / 2) - money : 0
}