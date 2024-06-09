
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    res = 0
    while b % a != 0 or c % b != 0:
        if b % a != 0:
            diff = b % a
            b += 1 if diff > 0 else -1
            res += 1
        if c % b != 0:
            diff = c % b
            c += 1 if diff > 0 else -1
            res += 1
    
    print(res)
    print(a, b, c)
