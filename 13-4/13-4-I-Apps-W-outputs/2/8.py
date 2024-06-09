
for i in range(int(input())):
    l, r = map(int, input().split())
    for x in range(l, r+1):
        for y in range(x, r+1):
            if y % x == 0:
                print(x, y)
                break

