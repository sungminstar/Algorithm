function solution(food) {
    var answer = '';
    for(let i = 1; i < food.length; i++) {
        for(let j = 0; j < Math.floor(food[i] / 2); j++){
            answer += String(i);
        }

    }
        let reversed = answer.split('').reverse().join('');
    answer = answer+'0'+reversed
    return answer;
}