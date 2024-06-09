
n = int(input())
visitors = []
for _ in range(n):
    h, m = map(int, input().split())
    visitors.append(h * 60 + m)

visitors.sort()

max_cashes = 0
current_cashes = 0
for v in visitors:
    if current_cashes == 0:
        current_cashes += 1
    else:
        if v - visitors[visitors.index(v) - 1] <= 20:
            current_cashes += 1
        else:
            max_cashes = max(max_cashes, current_cashes)
            current_cashes = 1

max_cashes = max(max_cashes, current_cashes)
print(max_cashes)
