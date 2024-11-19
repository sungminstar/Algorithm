from collections import deque

def solution(progresses, speeds):
    answer = []
    release = deque()

    for i in range(len(progresses)):
        days = (100 - progresses[i] + speeds[i] - 1) // speeds[i]  # 올림 계산
        release.append(days)

    while release:
        current = release.popleft()
        cnt = 1  
        while release and release[0] <= current:
            cnt += 1
            release.popleft()
        answer.append(cnt)

    return answer
