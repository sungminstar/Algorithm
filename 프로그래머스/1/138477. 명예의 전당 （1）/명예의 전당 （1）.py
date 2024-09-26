def solution(k, score):
    low_score = []
    day_score = []
    for i in range (len(score)) :
        day_score.append(score[i])
        day_score = sorted(day_score, reverse=True) 
        if len(day_score) > k:
            day_score = day_score[:k]
        low_score.append(day_score[-1])
    print(low_score)


    return low_score 