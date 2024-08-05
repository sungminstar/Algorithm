function solution(array, commands) {
    let answer = [];
    for(let i = 0; i < commands.length; i++){
        let sliceArray = array.slice(commands[i][0] - 1, commands[i][1]);
        sliceArray = sliceArray.sort((a, b) => a- b);
        answer[i] = sliceArray[commands[i][2] -1]
    }
    return answer;
}