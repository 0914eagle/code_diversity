
n, x, y = map(int, input().split())
s = input()

cost = 0
if '0' in s:
    groups = s.split('1')
    cost = y * (len(groups) - 1) + x

print(cost)
