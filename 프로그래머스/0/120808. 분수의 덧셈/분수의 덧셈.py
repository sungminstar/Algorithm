import math

#최소공배수
def get_lcm(a, b) :
    return (a * b) // math.gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    lcm = get_lcm(denom1, denom2)
    numer = numer1 * lcm // denom1 + numer2 * lcm // denom2
    answer_gcd = math.gcd(numer, lcm)
    return [numer //  answer_gcd, lcm // answer_gcd]