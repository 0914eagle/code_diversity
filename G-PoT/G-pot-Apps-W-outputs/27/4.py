
n = int(input())
visitors = []
for _ in range(n):
    h, m = map(int, input().split())
    visitors.append(h * 60 + m)

visitors.sort()

cashes = 1
max_cashes = 1
for i in range(1, n):
    if visitors[i] == visitors[i-1]:
        cashes += 1
    else:
        cashes = 1
    max_cashes = max(max_cashes, cashes)

print(max_cashes)
