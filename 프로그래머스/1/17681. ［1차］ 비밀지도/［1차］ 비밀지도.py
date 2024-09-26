def solution(n, arr1, arr2):
    arr1_n = []
    arr2_n = []
    answer = []
    for i in range(n) :
        arr1_n.append(bin(arr1[i])[2:].zfill(n))
        arr2_n.append(bin(arr2[i])[2:].zfill(n))
    for i in range(n) :
        temp = ""
        for j in range(n) :
            if arr1_n[i][j] == '1' or arr2_n[i][j] == '1' :
                temp += '#'
            else :
                temp += ' '
        answer.append(temp)
    return answer