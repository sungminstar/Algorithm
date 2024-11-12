def solution(array, commands):
    answer = []
    for i in range(len(commands)) :
        temp = sorted(array[commands[i][0]-1:commands[i][1]]);
        idx = commands[i][2]-1;
        answer.append(temp[idx])
    return answer