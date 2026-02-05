def solution(x):
    tmp = x
    num = 0
    
    while x > 0 :
        num += (x%10) 
        x //= 10
        
    return True if tmp % num == 0 else False
    
        