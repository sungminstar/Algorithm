function solution(s, n) {
    let ans = s.split('');
    let ascii = [];
    
    for (let i = 0; i < ans.length; i++) {
        let charCode = ans[i].charCodeAt(0);
        
        if (charCode === 32) {
            ascii.push(charCode);
        } else if (charCode >= 65 && charCode <= 90) {
            let newCharCode = (charCode - 65 + n) % 26 + 65;
            ascii.push(newCharCode);
        } else if (charCode >= 97 && charCode <= 122) {
            let newCharCode = (charCode - 97 + n) % 26 + 97;
            ascii.push(newCharCode);
        }
    }

    let str = String.fromCharCode(...ascii);
    return str;
}

