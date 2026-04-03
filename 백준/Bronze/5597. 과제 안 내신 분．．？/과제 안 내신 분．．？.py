arr = list(range(1, 31, 1))

for i in range(28) :
    n = int(input())
    if n in arr :
        arr.remove(n)

print(min(arr))
print(max(arr))
