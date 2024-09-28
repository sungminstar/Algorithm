def solution(number, limit, power):
    
    # 각 기사 : 자신의 기사 번호의 약수의 개수에 해당하는 공격력을 가진 무기 구매
        # 단, 공격력의 제한 수치 limit 보다 큰 공격력을 가진 무기를 구매하려면 
        # 지정 무기 power 공격력 구매해야 함
    
    # 1 ~ number 각각의 약수의 개수 구하기 => 배열
        # 이때, attack[i]의 약수의 개수 > limit : sum += power
    attack = []
    answer = 0
    for i in range(1, number + 1) :
        cnt = 0
        for j in range(1, int(i**(1/2)) + 1) :
             if i % j == 0:
                if j ** 2 == i:
                    cnt += 1  # 제곱수일 때
                else:
                    cnt += 2  # 대칭적인 약수 2개 카운트
        attack.append(cnt)
    for i in range(number) : 
        if attack[i] > limit :
            answer += power
        else :
            answer += attack[i]
                
    return answer