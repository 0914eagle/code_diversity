
def max_annoyance_level(h, c, coworkers):
    coworkers.sort(key=lambda x: x[1], reverse=True)
    max_annoyance = 0
    for i in range(h):
        coworkers[i % c] = (coworkers[i % c][0] + coworkers[i % c][1], coworkers[i % c][1])
        max_annoyance = max(max_annoyance, coworkers[i % c][0])
    return max_annoyance

# Input
h, c = map(int, input().split())
coworkers = [tuple(map(int, input().split())) for _ in range(c)]

# Output
print(max_annoyance_level(h, c, coworkers))
