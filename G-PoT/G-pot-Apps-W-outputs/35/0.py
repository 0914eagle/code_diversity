
a, b, c = map(int, input().split())

sticks = [a, b, c]
sticks.sort()

if sticks[0] + sticks[1] > sticks[2]:
    print(0)
else:
    print(sticks[2] - sticks[1] - sticks[0] + 1)
