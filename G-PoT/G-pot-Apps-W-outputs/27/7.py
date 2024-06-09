
n = int(input())
visitors = []
for _ in range(n):
    h, m = map(int, input().split())
    visitors.append(h * 60 + m)

visitors.sort()
cashes = 0
for i in range(n):
    if i == 0 or visitors[i] - visitors[i-1] > 15:
        cashes += 1

print(cashes)
