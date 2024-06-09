
h, c = map(int, input().split())
coworkers = []
for _ in range(c):
    a, d = map(int, input().split())
    coworkers.append((a, d))

coworkers.sort(key=lambda x: x[1], reverse=True)

def calculate_annoyance_level(h, coworkers):
    total_annoyance = 0
    for i in range(len(coworkers)):
        if h == 0:
            break
        a, d = coworkers[i]
        if h >= a:
            total_annoyance += a + (h - a) * d
            h = a - 1
        else:
            total_annoyance += h
            h = 0
    return total_annoyance

max_annoyance = 0
for i in range(1, h+1):
    max_annoyance = max(max_annoyance, calculate_annoyance_level(i, coworkers))

print(max_annoyance)
