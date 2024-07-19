// 0 개수 세기
function countZero(s) {
    let cnt = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '0') cnt += 1;
    }
    return cnt;
}
// 이진변환
function toBinary(length) {
    let answer = '';
    while (length > 0) {
        answer = (length % 2).toString() + answer;
        length = Math.floor(length / 2);
    }
    return answer;
}

function solution(s) {
    let answer = [0, 0]; 
    
    while (s !== '1') {
        let zeroCount = countZero(s);
        answer[1] += zeroCount;
        
        s = s.replace(/0/g, '');
        
        s = toBinary(s.length);
        
        answer[0] += 1;
    }
    
    return answer;
}

