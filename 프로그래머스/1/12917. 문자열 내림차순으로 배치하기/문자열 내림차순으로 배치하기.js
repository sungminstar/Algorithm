function solution(s) {
    let strToArr = s.split("");
    strToArr = strToArr.sort((a, b) => {
        // 내림차순으로 정렬하며, 대문자는 소문자보다 작게 간주합니다.
        if (a < b) return 1;
        if (a > b) return -1;
        return 0;
    });
    return strToArr.join("");
}