def solution(n):
    answer = ''
    st = "수박"
    for i in range(n) :
        answer += st[0] if i % 2 == 0 else st[1]
    return answer