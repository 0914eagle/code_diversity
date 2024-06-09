
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    
    res = 0
    while b % a != 0 or c % b != 0:
        if b % a != 0:
            diff = abs(b % a - a)
            if b % a < a:
                b += diff
            else:
                b -= diff
            res += diff
        
        if c % b != 0:
            diff = abs(c % b - b)
            if c % b < b:
                c += diff
            else:
                c -= diff
            res += diff
    
    print(res)
    print(a, b, c)
