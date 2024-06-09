
n, m = map(int, input().split())
candies = []
for _ in range(m):
    a, b = map(int, input().split())
    candies.append((a, b))

def min_time_to_deliver(candies, start):
    time = 0
    for a, b in candies:
        time += min(abs(start - a), n - abs(start - a)) + min(abs(a - b), n - abs(a - b)) + 1
    return time

result = []
for i in range(1, n+1):
    result.append(min_time_to_deliver(candies, i))

print(*result)
