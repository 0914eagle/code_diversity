
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    res = 0

    while b % a != 0 or c % b != 0:
        if b % a != 0:
            diff = (b // a + 1) * a - b
            b += diff
            res += diff

        if c % b != 0:
            diff = (c // b + 1) * b - c
            c += diff
            res += diff

    print(res)
    print(a, b, c)
