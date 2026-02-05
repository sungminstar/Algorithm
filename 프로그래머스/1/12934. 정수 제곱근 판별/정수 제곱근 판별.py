def solution (n) :
    if n < 0 :
        return -1
    r = int(n**0.5)
    if r * r == n :
        return (r+1) ** 2
    else :
        return -1