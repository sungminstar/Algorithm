def solution(name, yearning, photo):
    answer = []
    # key : name | val : yearning => 딕셔너리 만들기
    name_yearn_dic = dict(zip(name, yearning))
    print(name_yearn_dic)
    
    # photo에 있는 이름에 해당하는 값을 딕셔너리에서 찾아서 계산하기
    for i in range(len(photo)) :
        temp = 0
        for j in range(len(photo[i])) :
            temp += name_yearn_dic.get(photo[i][j], 0)
        answer.append(temp)
    return answer