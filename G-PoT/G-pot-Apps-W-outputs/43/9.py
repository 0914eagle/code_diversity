
h, c = map(int, input().split())
coworkers = []
for _ in range(c):
    a, d = map(int, input().split())
    coworkers.append((a, d))

coworkers.sort(key=lambda x: x[1], reverse=True)

max_annoyance = 0
for i in range(h):
    max_annoyance = max(max_annoyance, coworkers[i][0] + coworkers[i][1]*i)

print(max_annoyance)
