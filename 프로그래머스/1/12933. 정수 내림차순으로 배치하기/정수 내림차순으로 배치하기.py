def solution (n) :
    list = []
    ans = 0
    
    while n > 0 :
        list.append(n % 10)
        n //= 10
        
    list = sorted(list, reverse=True)
    
    for i in range(len(list)) :
        ans = ans * 10 + list[i]

    return ans

    
    