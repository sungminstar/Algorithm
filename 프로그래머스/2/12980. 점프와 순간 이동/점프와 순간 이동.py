def solution(num):
    jump_cnt = 0

    while num > 0:
        if num % 2 != 0:
            num -= 1
            jump_cnt += 1
        else:
            num //= 2

    return jump_cnt
