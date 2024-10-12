def solution(s):
    answer = 0
    x_cnt = 1
    y_cnt = 0
    i = 1
    x = s[0]  # 첫 번째 문자를 기준 문자로 설정
    
    while i < len(s):
        if s[i] == x:
            x_cnt += 1
        else:
            y_cnt += 1
            
        i += 1
        
        if x_cnt == y_cnt:
            answer += 1  # 구간 분리
            if i < len(s):  # 다음 기준 문자를 설정
                x = s[i]
                # print("after" ,x, i)
            x_cnt = 0  # x의 개수는 1로 설정
            y_cnt = 0  # y는 0으로 초기화
            
    # 마지막 남은 구간이 있다면 추가
    if x_cnt != y_cnt:
        answer += 1
    
    return answer
