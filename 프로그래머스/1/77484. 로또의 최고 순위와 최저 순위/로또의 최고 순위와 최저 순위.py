def solution(lottos, win_nums):
    answer = []
    check = 0
    zero = 0
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums :
            check += 1
        elif lottos[i] == 0 :
            zero += 1
    if (zero + check <= 1) :
        answer.append(6)
    else :
        answer.append(7 - (zero+check))
    if (check <= 1) : 
        answer.append(6)
    else :
        answer.append(7 - check)
    
    return answer