
for _ in range(int(input())):
    l, r = map(int, input().split())
    for x in range(l, r+1):
        if x != 1 and x % 2 == 0:
            y = x // 2
            break
    print(x, y)

