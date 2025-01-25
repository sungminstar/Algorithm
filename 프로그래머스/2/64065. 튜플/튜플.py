def solution(s):
    answer = []

    subjects = [list(map(int, subset.split(","))) for subset in s[2:-2].split("},{")]

    subjects.sort(key=len)

    for subset in subjects:
        for num in subset:
            if num not in answer:
                answer.append(num)

    return answer