def solution(absolutes, signs):
    for i in range(len(signs)) :
        if signs[i] :
            absolutes[i] *= 1
        else :
            absolutes[i] *= -1
    
    return sum(absolutes)