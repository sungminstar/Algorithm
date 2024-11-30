from collections import deque

def solution(priorities, location):
    queue = deque([(value, idx) for idx, value in enumerate(priorities)])
    rank = 0  

    while queue:
        current = queue.popleft()
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            rank += 1 
            if current[1] == location:  
                return rank
