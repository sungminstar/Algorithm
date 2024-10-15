def solution(keymap, targets):
    answer = []
    
    for i in range(len(targets)):
        cnt = 0
        for j in range(len(targets[i])):
            min_presses = 100
            for k in range(len(keymap)):
                if targets[i][j] in keymap[k]:
                    min_presses = min(min_presses, keymap[k].index(targets[i][j]) + 1)
            if min_presses != 100:
                cnt += min_presses
            else:
                cnt = -1
                break
        
        answer.append(cnt)

    return answer
