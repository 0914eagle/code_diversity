
h, c = map(int, input().split())
coworkers = []
for _ in range(c):
    a, d = map(int, input().split())
    coworkers.append((a, d))

coworkers.sort(key=lambda x: x[1])

def max_annoyance(h, coworkers):
    left, right = 0, 10**9
    while left < right:
        mid = (left + right) // 2
        total = 0
        for a, d in coworkers:
            if a > mid:
                continue
            diff = min((mid - a) // d + 1, h)
            total += a * diff + d * (diff * (diff - 1)) // 2
        if total > mid * h:
            right = mid
        else:
            left = mid + 1
    return left

print(max_annoyance(h, coworkers))
