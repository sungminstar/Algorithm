def solution(n):
    answer = [1, 1]
    for i in range (2, n):
        answer.append(answer[i-1]+answer[i-2])
    return answer[n-1] % 1234567