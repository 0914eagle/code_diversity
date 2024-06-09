
h, c = map(int, input().split())
coworkers = []
for _ in range(c):
    a, d = map(int, input().split())
    coworkers.append((a, d))

coworkers.sort(key=lambda x: x[1], reverse=True)

def calculate_annoyance_level(num_helps):
    annoyance_levels = []
    for a, d in coworkers:
        annoyance_levels.append(a + d * num_helps)
    return max(annoyance_levels)

left, right = 0, h
while left < right:
    mid = (left + right) // 2
    if calculate_annoyance_level(mid) < calculate_annoyance_level(mid + 1):
        right = mid
    else:
        left = mid + 1

print(calculate_annoyance_level(left))
