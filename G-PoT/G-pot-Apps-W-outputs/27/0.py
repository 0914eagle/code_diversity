
n = int(input())
visitors = []
for _ in range(n):
    h, m = map(int, input().split())
    visitors.append(h * 60 + m)

visitors.sort()

max_cashes = 0
current_cashes = 0
for i in range(n):
    if current_cashes == 0:
        current_cashes += 1
        max_cashes = max(max_cashes, current_cashes)
    else:
        if visitors[i] - visitors[i-1] <= 20:
            current_cashes += 1
            max_cashes = max(max_cashes, current_cashes)
        else:
            current_cashes = 1

print(max_cashes)
