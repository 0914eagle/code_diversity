
h, c = map(int, input().split())
coworkers = []
for _ in range(c):
    a, d = map(int, input().split())
    coworkers.append((a, d))

coworkers.sort(key=lambda x: x[1], reverse=True)

def max_annoyance(h, coworkers):
    max_annoyance_level = 0
    for i in range(1, h+1):
        total_annoyance = sum(max(0, a + d*(i-1)) for a, d in coworkers)
        max_annoyance_level = max(max_annoyance_level, total_annoyance)
    return max_annoyance_level

print(max_annoyance(h, coworkers))
