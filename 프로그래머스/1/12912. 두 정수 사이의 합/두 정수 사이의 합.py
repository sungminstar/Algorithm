def solution (a, b) :
    ans = 0
    if b < a :
        tmp = a
        a = b
        b = tmp
        
    for i in range(a, b+1) :
        ans += i
    return ans