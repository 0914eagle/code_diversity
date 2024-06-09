
for _ in range(int(input())):
    l, r = map(int, input().split())
    for x in range(l, r+1):
        if x > 1 and r % x == 0:
            print(x, r)
            break
    else:
        print(-1)

