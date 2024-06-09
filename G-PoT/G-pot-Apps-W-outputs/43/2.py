
h, c = map(int, input().split())
coworkers = []
for _ in range(c):
    a, d = map(int, input().split())
    coworkers.append((a, d))

coworkers.sort(key=lambda x: x[1], reverse=True)

total_annoyance = 0
max_annoyance = 0

for i in range(h):
    total_annoyance += coworkers[i][0] + i * coworkers[i][1]
    max_annoyance = max(max_annoyance, total_annoyance)

print(max_annoyance)
