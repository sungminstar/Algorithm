def solution(citations) :
    for i in range(max(citations) , -1, -1) :
        c = 0
        for j in citations :
            if j >= i : 
                c += 1
        if c >= i :
            return i
    return 0
        