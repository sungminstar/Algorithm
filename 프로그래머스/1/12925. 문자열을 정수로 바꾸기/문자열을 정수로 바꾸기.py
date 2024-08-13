def solution(s):
    sign = 1
    if s[0] == '-' : 
        sign = -1
        s = s[1:]
    return sign * int(s)