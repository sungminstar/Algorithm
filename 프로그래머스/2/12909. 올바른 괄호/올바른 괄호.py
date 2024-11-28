def solution(s):
    if len(s) == 0:
        return True

    stack = []
    stack.append(s[0])

    for i in range(1, len(s)):
        if stack and s[i] == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s[i])

    return len(stack) == 0
