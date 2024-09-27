def solution(cards1, cards2, goal):
    cards1_idx = 0
    cards2_idx = 0
    for i in range(0, len(goal)) :
        if cards1_idx < len(cards1) and goal[i] == cards1[cards1_idx] : 
            cards1_idx += 1
        elif cards2_idx < len(cards2) and goal[i] == cards2[cards2_idx] : 
            cards2_idx += 1
        else :
            return "No"
    return "Yes"