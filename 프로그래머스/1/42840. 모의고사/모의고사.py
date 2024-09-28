    # 1번 : 1 2 3 4 5 1 2 3 4 5 ...  
        # 1 : 0 , 5, 10, ... => 5로 나눈 나머지 = 0이 되는 indx : 5n
        # 2 : 1, 6, 11, ... => 5로 나눈 나머지 = 1이 되는 indx : 5n + 1
        # 3 : => 5로 나눈 나머지 = 2가 되는 indx : 5n + 2
        # 4 : => 5로 나눈 나머지 = 3이 되는 indx : 5n + 3
        # 5 : => 5로 나눈 나머지 = 4가 되는 indx : 5n + 4
def check1(answers) : 
    cnt = 0
    for i in range(len(answers)) :
        if answers[i] == 1 and i % 5 == 0 : cnt += 1
        elif answers[i] == 2 and i % 5 == 1 : cnt += 1
        elif answers[i] == 3 and i % 5 == 2 : cnt += 1
        elif answers[i] == 4 and i % 5 == 3 : cnt += 1
        elif answers[i] == 5 and i % 5 == 4 : cnt += 1
    return cnt

    # 2번 : 2 1 2 3 2 4 2 5 2 1 2 3 ... 
        # 2 : 0, 2, 4, ... => idx가 0부터 +2
        # 1 : 1, 9, 17, ... => idx가 1부터 +8 : 8n + 1 (n = 0, 1, ..)
        # 3 : 3, 11,  => 8n + 3 (n = 0, 1, 2, ...)
        # 4 : 8n + 5 
        # 5 : 8n + 7
def check2(answers) : 
    cnt = 0
    for i in range(len(answers)) :
        if answers[i] == 2 and i % 2 == 0 : cnt += 1
        elif answers[i] == 1 and i % 8 == 1 : cnt += 1
        elif answers[i] == 3 and i % 8 == 3 : cnt += 1
        elif answers[i] == 4 and i % 8 == 5 : cnt += 1
        elif answers[i] == 5 and i % 8 == 7 : cnt += 1
    return cnt
    # 3번 : 3 3 1 1 2 2 4 4 5 5 3 3 1 1 2 2 ... 
        # 3 : 0, 1, 10, 11, 20, 21, .. : 10n / 10n + 1
        # 1 : 2, 3, 12, 13, 22, 23, .. : 10n + 2 / 10n + 3
        # 2 : 10n + 4 / 10n + 5
        # 4 : 10n + 6 / 10n + 7
        # 5 : 10n + 8 / 10n + 9
def check3(answers) : 
    cnt = 0
    for i in range(len(answers)) :
        if answers[i] == 3 and (i % 10 == 0 or i % 10 == 1) : cnt += 1
        elif answers[i] == 1 and (i % 10 == 2 or i % 10 == 3) : cnt += 1
        elif answers[i] == 2 and (i % 10 == 4 or i % 10 == 5) : cnt += 1
        elif answers[i] == 4 and (i % 10 == 6 or i % 10 == 7) : cnt += 1
        elif answers[i] == 5 and (i % 10 == 8 or i % 10 == 9) : cnt += 1
    return cnt

def solution(answers):
    correct_cnt = []
    answer = []
    
    correct_cnt.append(check1(answers))
    correct_cnt.append(check2(answers))
    correct_cnt.append(check3(answers))
    
    maximum = max(correct_cnt)
    
    for i in range(3) : 
        if correct_cnt[i] == maximum : 
            answer.append(i+1)

    return answer