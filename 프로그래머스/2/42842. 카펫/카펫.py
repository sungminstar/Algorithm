import math 
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, int(math.sqrt(total))+1) :
        if total % i == 0:
            p = total // i
        else :
            continue
        if (p - 2) * (i - 2) == yellow:
            answer.append(p)
            answer.append(i)
            break
    answer.sort(reverse=True)
    return answer