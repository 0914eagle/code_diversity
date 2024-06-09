
n = int(input())

if n == 2:
    print(1)
else:
    k = 1
    while k * (k + 1) // 2 < n:
        k += 1
    print(k)
