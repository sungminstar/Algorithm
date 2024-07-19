function solution(s) {
    let sArr = s.split(" ");
    
    for (let i = 0; i < sArr.length; i++) {
        if (sArr[i].length > 0) {
            sArr[i] = sArr[i].toLowerCase();
            if (isNaN(sArr[i][0])) {
                sArr[i] = sArr[i][0].toUpperCase() + sArr[i].slice(1);
            }
        }
    }
    
    return sArr.join(" ");
}
