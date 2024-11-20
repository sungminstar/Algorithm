def solution(n, words):
    result = [0] * 2
    for i in range(1, len(words)) :
        if words[i-1][-1] != words[i][0] or words[i] in words[:i] :
            result[0] = i % n + 1
            result[1] = i // n + 1
            break
    return result