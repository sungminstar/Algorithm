def solution(num, total):
    # (start + (start+num-1)) * num // 2 = total
    # start = (total * 2 // num - num + 1 ) // 2
    start = (total * 2 // num - num + 1 ) // 2    
    return [start + i for i in range(num)]