def solution(sizes):
    answer = 0
    max_width = 0
    min_height = 0
    
    for i in range(len(sizes)) :
        if max_width >= max(sizes[i]) and min_height >= min(sizes[i]) :
            continue;
        else :
            if max_width <= max(sizes[i]) : 
                max_width = max(sizes[i])  
            if min_height <= min(sizes[i]) :
                min_height = min(sizes[i])    
    answer = max_width * min_height
    return answer