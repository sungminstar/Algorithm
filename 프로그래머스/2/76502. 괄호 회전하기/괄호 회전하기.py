def check_str(s):
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack: 
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '[' and char != ']') or (top == '{' and char != '}'):
                return False
    return len(stack) == 0


def solution(s):
    cnt = 0
    for i in range(len(s)) :
        tmp = s[0]
        s = s[1:len(s)]+tmp
        if check_str(s) :
            cnt += 1
    return cnt