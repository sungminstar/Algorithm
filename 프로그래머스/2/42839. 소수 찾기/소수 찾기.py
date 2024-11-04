from itertools import permutations
import math

def checkPrime(n) :
    cnt = 0
    if n < 2 :
        return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            return False
    return True

def solution(numbers) :
    combination = set()
    for i in range(1, len(numbers)+1) :
        for perm in permutations(numbers, i) :
            num = int("".join(perm))
            if(checkPrime(num)) :
                combination.add(num)
    print(combination)
    return len(combination)