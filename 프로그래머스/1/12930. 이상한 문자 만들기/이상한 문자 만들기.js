function solution(s) {
    let sArr = s.split(" ");
    for (let i = 0; i < sArr.length; i++) {
        let word = sArr[i].split('');
        for (let j = 0; j < word.length; j++) {
            if (j % 2 === 0) {
                word[j] = word[j].toUpperCase();
            } else {
                word[j] = word[j].toLowerCase();
            }
        }
        sArr[i] = word.join('');
    }
    return sArr.join(" ");
}

