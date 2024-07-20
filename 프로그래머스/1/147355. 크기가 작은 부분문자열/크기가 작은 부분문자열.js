function solution(t, p) {
    let subStr = [];
    for(let i = 0; i + p.length <= t.length; i++){
        subStr.push(t.substr(i, p.length));
    }
    subStr = subStr.filter((num) => parseInt(num) <= parseInt(p));
    return subStr.length;
}