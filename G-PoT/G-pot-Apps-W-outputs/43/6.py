
h, c = map(int, input().split())
coworkers = []
for _ in range(c):
    a, d = map(int, input().split())
    coworkers.append((a, d))

coworkers.sort(key=lambda x: x[1])

low = 0
high = 10**9

while low < high:
    mid = (low + high) // 2
    total = 0
    for a, d in coworkers:
        if a > mid:
            break
        total += min((mid - a) // d + 1, h)
    
    if total < h:
        low = mid + 1
    else:
        high = mid

print(low)
