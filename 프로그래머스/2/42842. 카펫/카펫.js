function solution(brown, yellow) {
    let answer = [0, 0];
    for(let i = 1; i <= Math.sqrt(yellow); i++){
        if(yellow % i === 0) {
            let width = i;
            let height = yellow/i;
            if((width+2) * (height + 2) == brown + yellow) {
                answer[0] = Math.max(width+2, height+2);
                answer[1] = Math.min(width+2, height+2);
            }
        } 
    }
    return answer;
}