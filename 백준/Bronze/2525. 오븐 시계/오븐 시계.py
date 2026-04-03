a, b = map(int, input().split())
c = int(input())

c_a = c // 60
c_b = c % 60

a += c_a
b += c_b

if b >= 60 :
    b -= 60
    a += 1

if a >= 24 :
    a -= 24

print(a, b)

